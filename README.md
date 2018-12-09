#data-stream

Usage:
  python3.7 <configuration_dir> [-t <target_server>] [-p <target_port>] [-i <interval>] [-s <data_save_path>]


keeps generate data and send by TCP, and save data in save_path

Ctrl-C will terminate sending


interval(sec) : generate & send data with defined interval. if not specified, interval value is 1 second

configuration_dir : directory where 'data.config.json' exists (See data.config.template.json'
  maximum_data_count : total number of data
  specific_data_types : multiple objects specifying data
    {
      type : type of data(int,long,string)
      count : number of values with type
      length : size of data(int,long : max value/string : length of string)
    }
  major_data_type : type of remaining data values (non-specific)
  major_data_length : size of remaining data values


