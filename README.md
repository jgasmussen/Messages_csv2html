# Messages_csv2html BETA Version 0.2
This python script takes SMS, MMS, Text Messages, & Chats that are stored in .csv file format and converts it to an HTML Message Thread.

First, make sure your .csv file matches the expected fields (Direction, Sender, Message, Time_Local). You can customize the fields by editing lines 61-68.


Next, make sure the script's file permissions are set as executable:

```
$ sudo chmod +x Messages_csv2html.py
```

Finally, run the script using the following syntax:
```
$ python3 Messages_csv_2_html.py [input_filename.csv] [output_filename.html] 
```
The input_filename.csv should be changed to the filename of the .csv file you want to read from.
The output_filename.html is the name of the webpage you want your report to be written to.

-----------------------------------------------------------------------------------------------------------------------------------------------------------

FUTURE PLANS AND UPDATES:
- Add support for Emoji's, gifs, pics, videos, and other file attachments.
- *FIXED - Beta Version 0.2* Formatting the message thread containers to be offset to the sides (outgoing on right side and incoming on left side).
- Link to Contact database to use stored contact names instead of raw telephone numbers.

If you discover any bugs or have a feature request please create an issue and/or send me a message.
