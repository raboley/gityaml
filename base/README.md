# Python Base Container Image

This container is a lightweight python 3 image based on the ubuntu:trusty os image.

## Errors and Troubleshooting

If you get an error saying 

``` bash
Error Script directory doesnt exist
```

Or something like that, make sure that the **entrypoint.sh** script has the LF line endings. Since this is going to be run in a linux container, if it has the default CRLF line endings windows uses, it will error. What happens is the bash bang at the top gets read as

```
#!/bin/bash<M
```

That makes the container look for a file called bash<M which doesn't exist. So to make sure things still work, set the line endings to LF, which can be done in vscode by opening the file then using the command pallete `ctrl + shift + p` and `change end of line sequence` and select `LF`.