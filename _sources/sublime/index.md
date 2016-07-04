---
title: SublimeText3
sorting: A
---

Sublime Text 3
==============

### How to ignore files and/or dirs in projects?

```json
{
    "folders":
    [
        {
            "path": "src",
            "folder_exclude_patterns": ["backup"],
            "follow_symlinks": true
        },
        {
            "path": "docs",
            "file_exclude_patterns": ["*.tmp"]
        }
    ]
}
```

Read more:

- https://www.sublimetext.com/docs/3/projects.html

### Related links

- https://www.sublimetext.com/docs/3/index.html