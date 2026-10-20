# OSMetaClass

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class OSMetaClass : OSMetaClassBase
```

## Topics

### Instance Methods
- [- alloc](./osmetaclass/api-1452498-alloc.md)
- [- checkMetaCast](./osmetaclass/api-1452582-checkmetacast.md)
- [- getClassName](./osmetaclass/api-1452466-getclassname.md)
- [- getClassNameSymbol](./osmetaclass/api-1452546-getclassnamesymbol.md)
- [- getClassSize](./osmetaclass/api-1452517-getclasssize.md)
- [- getInstanceCount](./osmetaclass/api-1452533-getinstancecount.md)
- [- getKmodName](./osmetaclass/api-1452511-getkmodname.md)
- [- getMetaClass](./osmetaclass/api-1452527-getmetaclass.md)
- [- getRetainCount](./osmetaclass/api-1452500-getretaincount.md)
- [- getSuperClass](./osmetaclass/api-1452480-getsuperclass.md)
- [- instanceConstructed](./osmetaclass/api-1452567-instanceconstructed.md)
- [- instanceDestructed](./osmetaclass/api-1452574-instancedestructed.md)
- [- release](./osmetaclass/api-1452475-release.md)
- [- release](./osmetaclass/api-3437949-release.md)
- [- reservedCalled](./osmetaclass/api-1452552-reservedcalled.md)
- [- retain](./osmetaclass/api-1452463-retain.md)
- [- serialize](./osmetaclass/api-1452563-serialize.md)
- [- taggedRelease](./osmetaclass/api-1452456-taggedrelease.md)
- [- taggedRelease](./osmetaclass/api-3437950-taggedrelease.md)
- [- taggedRetain](./osmetaclass/api-1452554-taggedretain.md)
### Type Methods
- [+ allocClassWithName](./osmetaclass/api-1452557-allocclasswithname.md)
- [+ allocClassWithName](./osmetaclass/api-3437945-allocclasswithname.md)
- [+ allocClassWithName](./osmetaclass/api-3437946-allocclasswithname.md)
- [+ checkMetaCastWithName](./osmetaclass/api-1452565-checkmetacastwithname.md)
- [+ checkMetaCastWithName](./osmetaclass/api-3437947-checkmetacastwithname.md)
- [+ checkMetaCastWithName](./osmetaclass/api-3437948-checkmetacastwithname.md)
- [+ checkModLoad](./osmetaclass/api-1452520-checkmodload.md)
- [+ considerUnloads](./osmetaclass/api-1452525-considerunloads.md)
- [+ getClassDictionary](./osmetaclass/api-1452544-getclassdictionary.md)
- [+ getMetaClassWithName](./osmetaclass/api-1452542-getmetaclasswithname.md)
- [+ logError](./osmetaclass/api-1452454-logerror.md)
- [+ modHasInstance](./osmetaclass/api-1452458-modhasinstance.md)
- [+ postModLoad](./osmetaclass/api-1452541-postmodload.md)
- [+ preModLoad](./osmetaclass/api-1452478-premodload.md)
- [+ printInstanceCounts](./osmetaclass/api-1452473-printinstancecounts.md)
- [+ reportModInstances](./osmetaclass/api-1452450-reportmodinstances.md)
- [+ serializeClassDictionary](./osmetaclass/api-1452436-serializeclassdictionary.md)

## Relationships

### Inherits From
- [OSMetaClassBase](./osmetaclassbase.md)

## See Also

### Base Types
- [OSSymbol](./ossymbol.md)
  OSSymbol wraps a C string in a unique C++ object for use as keys in Libkern collections.
- [OSObject](./osobject.md)
  OSObject is the concrete root class of the Libkern and I/O Kit C++ class hierarchy.
- [OSMetaClassBase](./osmetaclassbase.md)
  OSMetaClassBase is the abstract bootstrap class for the Libkern and I/O Kit run-time type information system.
- [OSObjectPtr](./osobjectptr.md)
- [OSObjectRef](./osobjectref.md)
- [Additional Types](./libkern/data_types/additional_types.md)
  Find custom type definitions and pointer types for standard classes. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osmetaclass)*