---
layout: post
title:  "Jupyter Notebook Server running in Ubuntu under WSL2 inaccessible from Windows 10 Pro"
date:   2021-09-27 10:00:00 +0600
author: Nick Jalbert
---

Small note on a quick fix:

I was running a Jupyter Notebook Server in Ubuntu under WSL2 on a Windows 10
Pro machine, and I was trying to navigate to the server's homepage.
Unfortunately, my browser could not reach the server.  After some tinkering, I
found a post suggesting that the WSL2 networking stack occasionally fails to
initialize fully.

The fix was:

* Close down all my Ubuntu terminals
* CTRL+SHIFT+ESC to the Task Manager
* Click to the Services tab
* Right click LxssManager and choose restart (this incidentally also killed
  Docker).
* Re-open my terminals
