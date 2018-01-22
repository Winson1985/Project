
'''This module is used to plot data struct and I/O routines'''

# Result data struct
class Channel():
    def __init__(self):
        self.varname = ""
        self.varunit = ""
        self.values = []

# class OutputData
class OutputData():
    '''OutputData class'''

    # read input file
    def read_input_file(self, filename):
        '''Read result file'''
        filedata = []
        try:
            with open(filename, 'r') as inputfile:
                filedata = inputfile.readlines()
        except FileNotFoundError:
            print("Error: File " + filename + " not exist!")
        else:
            print("File <" + filename + "> opened")
        return filedata

    # Returns channel list from filedata
    def get_channel_list(self, filedata):
        '''Returns channel list from filedata'''
        i = -1
        startline = -1
        varnames = []
        varunits = []
        for line in filedata:
            i += 1
            if line.find("Time") != -1:
                startline = i
                break
        channel_list = []
        if startline != -1:
            varnames = filedata[startline].split()
            varunits = filedata[startline+1].split()
            self.channel_dict = {}
            i = 0
            for varname in varnames:
                i += 1
                self.channel_dict.setdefault(varname, i)
            num_channels = len(varnames)
            endline = len(filedata)
            
            # input var names and units
            for ichan in range(num_channels):
                channel = Channel()
                channel.varname = varnames[ichan]
                channel.varunit = varunits[ichan]
                channel_list.append(channel)
            # input values of channels
            for i in range(startline+2, endline):
                line = filedata[i]
                list = line.split()
                ichan = 0
                for value in list:
                    data = float(value)
                    channel_list[ichan].values.append(data)
                    ichan += 1
        return channel_list

    # Constructor 
    def __init__(self, filename):
        self.inpfilename = filename
        # gets file data from input file
        self.filedata = self.read_input_file(self.inpfilename)
        # gets data list from filedata
        self.channel_list = self.get_channel_list(self.filedata)

        # gets output folder path (to improve)
        self.path = "channel_plots"

    # Generates Gunplot file
    def gunplot(self, channel, si):
        filename = channel.varname + ".gpl"
        write_output = []
        with open(filename, 'w') as outputfile:
            path = "C:\\qiuyo\Documents\Projects\Codes\Project\Project\PlotOutData\PlotOutData"
            line = "set loadpath " + '"' + path + '"'
            write_output.append(line)
            line = "set xlabel " + '"Time [sec]"'
            write_output.append(line)
            line = "set ylabel " + \
                   '"' + channel.varname + " " + channel.varunit + '"'
            write_output.append(line)
            line = "plot " + '"'+self.inpfilename+'"' + " using " + "1:($" + \
                   str(self.channel_dict[channel.varname]) +")" + \
                   " with lines title " + '"' + channel.varname + '"'
            write_output.append(line)
            for line in write_output:
                outputfile.write(line+"\n")

    def plot_channels(self, si):
        # Generate output file folder
        import os
        #os.mkdir(self.path)
        # plots each channel
        for ichan in range(1, len(self.channel_list)):
            self.gunplot(self.channel_list[ichan], si)


        



