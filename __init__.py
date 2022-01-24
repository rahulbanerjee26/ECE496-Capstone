from bitalino import BITalino
import time
from pandas import read_csv
from matplotlib import pyplot
import pandas

def collect_data(macAddress,run_time=2,channels=[3],samplingRate=100,nSamples=1,saveData=True,outputFileName='ppgData'):
    # Connect to BITalino
    device = BITalino(macAddress)
    ppg_data = []
    times = []
    # Start Acquisition
    device.start(samplingRate, channels)
    start = time.time()
    end = time.time()
    while (end - start) < run_time:
        '''
        The return value is a matrix like below
        [
            [sequence_num,digital1_val,digital2_val,digital3_val,digital4_val,..analog_channels],

        ]
        '''
        times.append(end-start)
        ppg_data.extend(device.read(nSamples))
        end = time.time()
    # Stop acquisition
    device.stop()
    # Close connection
    device.close()

    channel4_data = []
    for data in ppg_data:
        channel4_data.append(data[-1])
    ppg_vs_time = zip(times,channel4_data)

    if saveData:
            with open(f'PPG_Data/{outputFileName}.csv','w') as file:
                for ppg_time,ppg_value in ppg_vs_time:
                 file.write(f'{ppg_time},{ppg_value}\n')
            print('Collected Data') 
    return ppg_vs_time

def plot_time_series(ppg_data=None,path=''):
    if not (ppg_data or path):
        raise Exception('Please provide data or path to csv file')
    if path: data = read_csv(path,header=0, index_col=0)
    else: data = ppg_data

    data.plot(legend=None)
    pyplot.title(outputFileName)
    pyplot.xlabel('Time')
    pyplot.ylabel('PPG Value')
    pyplot.savefig(f'PPG_Data/{outputFileName}.png')
    pyplot.show()
    

if __name__ == '__main__':
    # Windows : "XX:XX:XX:XX:XX:XX"
    # Mac OS :  "/dev/tty.BITalino-XX-XX-DevB" or "/dev/tty.BITalino-DevB" 
    macAddress = "/dev/tty.BITalino-DevB"
    name = 'Rahul'
    outputFileName = f'{name}_PPG_Data'
    ppg_vs_time = collect_data(macAddress,outputFileName=outputFileName)
    plot_time_series(path=f'PPG_Data/{outputFileName}.csv')

