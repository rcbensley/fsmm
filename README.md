FSMM
----

Tool to download mods from [the mod hub](https://www.farming-simulator.com/mods.php?lang=en&country=gb) straight into the default FS19 mods dir.

##  Install
If your Documents\saved games\FS19 directory is not in the default path, just run this tool from within the directory, called "mods".

##  Usage
To use the tool, drag and drop the mods list text file onto fsmm.exe or parse it as the first parameter:

```fsmm.exe mods_list.txt```

## Mods list format
The mod list is a plain text file, formatted with the link to to the mod page on one line, and the download link on the next line.

Example:
```
https://www.farming-simulator.com/mod.php?lang=en&country=gb&mod_id=118906&title=fs2019
https://cdn10.giants-software.com/modHub/storage/00118906/FS19_flieglDPW180.zip
https://www.farming-simulator.com/mod.php?lang=en&country=gb&mod_id=137675&title=fs2019
https://cdn5.giants-software.com/modHub/storage/00137675/FS19_hauerSnowPack.zip
```

