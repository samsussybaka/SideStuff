package com.samcum;

import java.util.logging.Logger;
import org.bukkit.plugin.java.JavaPlugin;

/*
 * bbcslasher java plugin
 */
public class Plugin extends JavaPlugin
{
  private static final Logger LOGGER=Logger.getLogger("bbcslasher");

  public void onEnable()
  {
    LOGGER.info("bbcslasher enabled");
  }

  public void onDisable()
  {
    LOGGER.info("bbcslasher disabled");
  }
}
