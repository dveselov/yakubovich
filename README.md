# yakubovich
Fallout 2 savefile reader/writer

# Usage
```python
import yakubovich

save = yakubovich.read("SAVE.DAT", "cp1251")
print(save)

"""
{
    'savefile': {
        'name': 'autosave',
        'date': (20, 7, 2016, 36)
    },
    'game': {
        'map': {
            'number': 15,
            'name': 'VCTYCTYD.sav',
            'level': 0
        }, 
        'date': (9, 9, 2241, 40422771)
    },
    'player': {
        'name': 'Чица'
    }
}
"""
```
