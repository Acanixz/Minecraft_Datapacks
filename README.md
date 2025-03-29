# Minecraft_Datapacks
This is a repository containing a Minecraft Dedicated Server setup for datapack development on Windows. It contains 3 different configurations to initialize the server. 

The datapacks are loaded consistently by linking all ``/datapacks`` folders from each world to the ``Datapacks`` folders via symbolic links.

# Avaliable configurations

1. ``Run_World.py`` - Runs the server in a fixed ``world`` save, default generation
2. ``Run_Superflat.py`` - Runs the server in a fixed ``superflat`` save, flat generation
3. ``Run_Temporary.py`` - Runs the server in a ``temporary`` save that gets erased before execution, default generation

# Installation Instructions

1. Run ``Setup.py``, this will create the folders and symlinks required for the ``Datapacks`` folder to work
    - Note: This script will ask for administrator priviledges as symlinks can't be created without it
2. Download ``server.jar`` from the Minecraft version you want to run
    - Recommended 1.21.x and above
    - You can find the file through one of the following links:
        - https://www.minecraft.net/en-us/download/server
        - https://minecraft.wiki/w/Java_Edition_1.21.5
            - The download is in the infobox on the right
            - You can find server files from older versions using this method
3. Move your ``server.jar`` file into the ``Server`` directory and execute ``Run.bat``
    - Check the [wiki](https://minecraft.wiki/w/Tutorial:Setting_up_a_Java_Edition_server#Startup_script) if it fails to run or you want to modify parameters/RAM usage

4. Accept the EULA by changing ``eula.txt``
5. Change server.properties to your liking
    - The following properties will be overwritten when using the python scripts, no need to change them
        - level-name
        - level-type
    - Noteworthy changes: (from personal testing)

        | Property | Description |
        | -- | -- |
        | enable-command-block | This is required for command blocks to run |
        | online-mode | If you plan on using offline mode alts or pirated players to test, turn this on. NOTE: This will allow ANYONE to join as YOU, careful with OP players|
        | spawn-protection | This may be annoying if you need to test with other non-OP players, as blocks near spawn will be unbreakable for them |
    - You can find more info about ``server.properties`` on the [wiki](https://minecraft.wiki/w/Server.properties)
6. **Done!** you can now run one of the python scripts to start the server!
    - NOTE: You can only run ONE script at a time. If you want to change maps you'll have to ``stop`` the server and execute the other script.
    - ``Setup.py`` is no longer needed if the symlinks are set correctly, you can delete it if you want to
