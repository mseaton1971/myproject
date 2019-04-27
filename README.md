I will support the following:

sish will support basic linux/unix commands such as ls, date, echo, pwd, cat, etc.

Redirection:

sish supports the following three input-/output- redirection operators:

> file Redirect standard output to file.
>> file Append standard output to file. 
< file Redirect standard input from file.

Builtins:

sish will support the following builtins (which will take precedence over any non-builtin commands):

cd [dir]- Change the current working directory. If dir is not specified, change to the user’s home
          directory.

echo [word]- Print the given word, followed by a ’\n’. The following special values are supported:

exit- Exit the current shell.

I will implement as much of the popular unix commamds on the command line as possible.
