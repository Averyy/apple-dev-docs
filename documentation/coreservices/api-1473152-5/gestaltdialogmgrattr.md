# gestaltDialogMgrAttr

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltDialogMgrAttr = 'dlog'
```

#### Discussion

The `Gestalt` selector passed to determine what features of the Dialog Manager are present. This selector is available with Mac OS 8.5 and later. Passing `gestaltDialogManagerAttr` produces a 32-bit value whose bits you should test to determine what Dialog Manager functionality is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1473152-5/gestaltdialogmgrattr)*