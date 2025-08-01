# M.I.A-Tasks

### Code explanation of the first task

Firstly, I import the time library so I can use the delay function in the output
Then, I make the display_gear function which make the empty grid and put spaces between each row
Then, I have simulate the grid as a chars as follows: where a indicates top horizontal segment, b indicates top-right vertical segment, c indicates bottom-right vertical segment, d indicates bottom horizontal segment, bottom-left vertical segment, f indicates top-left vertical segment and g indicates middle horizontal segment
Then, I make a segment to light list which retrieves the list of segments for the given gear_number
Then, I have used the join function so convert each row into a string and can print it where if I don’t do this the output of the rows will be like this: ['#', '#', '#', ' ']
Then, I have made the animate range that takes the start gear and the end with a constant delay of about 0.5, If the user inputs the start gear smaller than the end (within the range) the step will be 1 else the step will be -1.
Then, I created a for loop that print the gear within the display range and apply the delay 0.5
Then, the while true to perform and endless loop until the user input the letter (q) and use the .split function to can read the input of the user that separated by a space


### Code explanation of the Second task
Firstly creating the encode function and I used (|||) as a separator to separate between the each string and change the list to a big string then send this string to decode function and separate between the substrings based on ||| separator
Then, create a function that takes the input from the user and create a terminator that I think that It will not be used, {I have a second approach to use (ctrl+z) as a terminator but I thought that the commander uses radio so no sense to use a command for laptops}.
Then, in the main function I handle that If the commander didn’t send any command if he didn’t send any thing (literally) then I print the outputs as mentioned in the example you gives me



