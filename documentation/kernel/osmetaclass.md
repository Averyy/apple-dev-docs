# OSMetaClass

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSMetaClass : OSMetaClassBase
```

## Topics

### Instance Methods
- [- alloc](osmetaclass/1452498-alloc.md)
- [- checkMetaCast](osmetaclass/1452582-checkmetacast.md)
- [- getClassName](osmetaclass/1452466-getclassname.md)
- [- getClassNameSymbol](osmetaclass/1452546-getclassnamesymbol.md)
- [- getClassSize](osmetaclass/1452517-getclasssize.md)
- [- getInstanceCount](osmetaclass/1452533-getinstancecount.md)
- [- getKmodName](osmetaclass/1452511-getkmodname.md)
- [- getMetaClass](osmetaclass/1452527-getmetaclass.md)
- [- getRetainCount](osmetaclass/1452500-getretaincount.md)
- [- getSuperClass](osmetaclass/1452480-getsuperclass.md)
- [- instanceConstructed](osmetaclass/1452567-instanceconstructed.md)
- [- instanceDestructed](osmetaclass/1452574-instancedestructed.md)
- [- release](osmetaclass/1452475-release.md)
- [- release](osmetaclass/3437949-release.md)
- [- reservedCalled](osmetaclass/1452552-reservedcalled.md)
- [- retain](osmetaclass/1452463-retain.md)
- [- serialize](osmetaclass/1452563-serialize.md)
- [- taggedRelease](osmetaclass/1452456-taggedrelease.md)
- [- taggedRelease](osmetaclass/3437950-taggedrelease.md)
- [- taggedRetain](osmetaclass/1452554-taggedretain.md)
### Type Methods
- [+ allocClassWithName](osmetaclass/1452557-allocclasswithname.md)
- [+ allocClassWithName](osmetaclass/3437945-allocclasswithname.md)
- [+ allocClassWithName](osmetaclass/3437946-allocclasswithname.md)
- [+ checkMetaCastWithName](osmetaclass/1452565-checkmetacastwithname.md)
- [+ checkMetaCastWithName](osmetaclass/3437947-checkmetacastwithname.md)
- [+ checkMetaCastWithName](osmetaclass/3437948-checkmetacastwithname.md)
- [+ checkModLoad](osmetaclass/1452520-checkmodload.md)
- [+ considerUnloads](osmetaclass/1452525-considerunloads.md)
- [+ getClassDictionary](osmetaclass/1452544-getclassdictionary.md)
- [+ getMetaClassWithName](osmetaclass/1452542-getmetaclasswithname.md)
- [+ logError](osmetaclass/1452454-logerror.md)
- [+ modHasInstance](osmetaclass/1452458-modhasinstance.md)
- [+ postModLoad](osmetaclass/1452541-postmodload.md)
- [+ preModLoad](osmetaclass/1452478-premodload.md)
- [+ printInstanceCounts](osmetaclass/1452473-printinstancecounts.md)
- [+ reportModInstances](osmetaclass/1452450-reportmodinstances.md)
- [+ serializeClassDictionary](osmetaclass/1452436-serializeclassdictionary.md)

## Relationships

### Inherits From
- [OSMetaClassBase](osmetaclassbase.md)

## See Also

- [OSSymbol](ossymbol.md)
  OSSymbol wraps a C string in a unique C++ object for use as keys in Libkern collections.
- [OSObject](osobject.md)
  OSObject is the concrete root class of the Libkern and I/O Kit C++ class hierarchy.
- [OSMetaClassBase](osmetaclassbase.md)
  OSMetaClassBase is the abstract bootstrap class for the Libkern and I/O Kit run-time type information system.
- [OSObjectPtr](osobjectptr.md)
- [OSObjectRef](osobjectref.md)
- [Additional Types](libkern/data_types/additional_types.md)
  Find custom type definitions and pointer types for standard classes. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osmetaclass)*