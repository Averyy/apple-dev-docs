# FSPathCopyObjectSync

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.8

## Declaration

```c
OSStatus FSPathCopyObjectSync(const char *sourcePath, const char *destDirPath, CFStringRef destName, char **targetPath, OptionBits options);
```

## See Also

### High-Level File Operations
- [FSFileOperationCopyStatus](./api-1566279-fsfileoperationcopystatus.md)
- [FSPathFileOperationCopyStatus](./api-1566335-fspathfileoperationcopystatus.md)
- [FSCopyObjectAsync](./api-1566285-fscopyobjectasync.md)
- [FSMoveObjectAsync](./api-1566762-fsmoveobjectasync.md)
- [FSPathCopyObjectAsync](./api-1566056-fspathcopyobjectasync.md)
- [FSPathMoveObjectAsync](./api-1566169-fspathmoveobjectasync.md)
- [FSFileOperationCancel](./api-1565866-fsfileoperationcancel.md)
- [FSFileOperationCreate](./api-1566666-fsfileoperationcreate.md)
- [FSFileOperationGetTypeID](./api-1565673-fsfileoperationgettypeid.md)
- [FSFileOperationScheduleWithRunLoop](./api-1565845-fsfileoperationschedulewithrunlo.md)
- [FSFileOperationUnscheduleFromRunLoop](./api-1565483-fsfileoperationunschedulefromrun.md)
- [FSCopyObjectSync](./api-1565258-fscopyobjectsync.md)
- [FSMoveObjectSync](./api-1566525-fsmoveobjectsync.md)
- [FSPathMoveObjectSync](./api-1566022-fspathmoveobjectsync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1565384-fspathcopyobjectsync)*