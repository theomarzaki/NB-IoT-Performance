import torch
import numpy as np

#takes action based on the output of the reinforcement learning model, Sending AT commands to the module to set the configurations
def takeAction(action_tensor,module):
    do_nothing = torch.tensor([1,0,0,0,0]).float()
    increase_timer = torch.tensor([0,1,0,0,0]).float()
    decrease_timer = torch.tensor([0,0,1,0,0]).float()
    increase_packet_size = torch.tensor([0,0,0,1,0]).float()
    decrease_packet_size = torch.tensor([0,0,0,0,1]).float()

    if torch.equal(action_tensor,increase_packet_size):
        previous_packet = module.command('AT+KIPOPT?')
        module.command('AT+KIPOPT={}'.format(previous_packet + 64)) #2^6 packet size increase
        print("increase packet size")
    elif torch.equal(action_tensor,decrease_packet_size):
        previous_packet = module.command('AT+KIPOPT?')
        module.command('AT+KIPOPT={}'.format(previous_packet - 64)) #2^6 packet size decrease
        print("decrease packet size")
    elif torch.equal(action_tensor,decrease_timer):
        previous_timer = module.Command('AT+CPSMS?')
        new_timer = "{0:b}".format(int(previous_timer) - 2)
        module.Command('AT+CPSMS={}'.format(new_timer))
        print("decrease timer")
    elif torch.equal(action_tensor,increase_timer):
        previous_timer = module.Command('AT+CPSMS?')
        new_timer = "{0:b}".format(int(previous_timer) + 2)
        module.Command('AT+CPSMS={}'.format(new_timer))
        print("increase timer")
    elif torch.equal(action_tensor,do_nothing):
        print("Do Nothing")
        pass
    else:
        pass

#Defines a min max scaler to preprocess the variables, to match the processing used by predictive models
def MinMaxScaler(scaler,input):
    input = np.array(input)
    x_std = (input - scaler.min_) / (scaler.data_range_ + scaler.min_) - scaler.min_
    x_scaled = x_std * ((scaler.data_range_ + scaler.min_) - scaler.min_) + scaler.min_
    return x_scaled

#preforms AT commands to obtain the parameters of the device
def getFeatures(module):
    ec = 0.30    #module.Command('AT') MODULE SPECIFIC
    ms = 2698.84   #module.Command('AT') MODULE SPECIFIC
    ecl = 0.38    #module.Command('AT') MODULE SPECIFIC
    location_coverage = module.Command('AT+CSQ')
    active_timer = module.Command('AT+CPSMS?')
    tau = module.Command('AT+CEREG?')
    current = 74372.5  #module.Command('AT') MODULE SPECIFIC
    duration_of_packet = 3085.4 #mean from dataset
    packet_size = module.command('AT+KIPOPT=')
    interval_of_packet = float(input("Average interval between packets: "))

    return [ec,ms,current_max,ecl,location,duration_of_packet,interval_of_packet,packet_size,active_timer,tau]
