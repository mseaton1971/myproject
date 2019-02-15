char* Testcgi
{
   int n;
   char* reply = NULL;
   n = strncasecmp(pathname, "/cgi-bin/", 9)

   if(n == 0 && cFlag != NULL)
   {

     fullpath = (char*)malloc(sizeof(char) * (strlen(cFlag) + strlen(&pathname[9]) + 2));
     strcat(fullpath, cFlag);
     strcat(fullpath, "/");
     strcat(fullpath, &pathname[9]);
 
     printf(fullpath);

     if(stat(fullpath, &statinfo) != 0)
     {
       free(fullpath);
       reply = "404 Not Found";
       return reply;
     }

     dup2(fd, STDOUT_FILENO);
     dup2(fd, STDERR_FILENO);
   }
   return reply;
}


