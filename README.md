# osu! seasonal backgrounds downloader
small python script to download seasonal backgrounds that show up in the client.  
pass folder to the python script. if you want to clean up old backgrounds add --remove-old (**DANGER:** will delete every file in that folder)

i also included example systemd units to automatically download backgrounds every 3 months. modify .service to point to your script path and folder.
