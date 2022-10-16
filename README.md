# csv2html
This python script takes SMS, MMS, Text Messages, & Chats that are stored in .csv file format and converts it to an HTML Message Thread

First, make sure your .csv file matches the expected fields (Direction, Sender, Message, Time_Local). You can customize the fields by editing lines 61-68.

Next, make sure the script's file permissions are set as executable:

```
$ sudo chmod +x Messages_csv2html.py
```

Finally, run the script using the following syntax:
```
$ python3 Messages_csv_2_html.py [input_filename.csv] [output_filename.html] 
