# OSClassDescription

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
struct OSClassDescription
```

```c
struct OSClassDescription {
    ...
};
```

## Topics

### Initializers
- [init()](./osclassdescription/api-3757893-init.md)
- [init(descriptionSize: UInt32, name: (CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar), superName: (CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar), methodOptionsSize: UInt32, methodOptionsOffset: UInt32, metaMethodOptionsSize: UInt32, metaMethodOptionsOffset: UInt32, queueNamesSize: UInt32, queueNamesOffset: UInt32, methodNamesSize: UInt32, methodNamesOffset: UInt32, metaMethodNamesSize: UInt32, metaMethodNamesOffset: UInt32, flags: UInt64, resv1: (UInt64, UInt64, UInt64, UInt64, UInt64, UInt64, UInt64, UInt64), methodOptions: (), metaMethodOptions: (), dispatchNames: (), methodNames: (), metaMethodNames: ())](./osclassdescription/api-3757894-init.md)
### Instance Properties
- [var descriptionSize: UInt32](./osclassdescription/api-3074891-descriptionsize.md)
- [var dispatchNames: ()](./osclassdescription/api-3074892-dispatchnames.md)
- [var flags: UInt64](./osclassdescription/api-3074893-flags.md)
- [var metaMethodNames: ()](./osclassdescription/api-3074894-metamethodnames.md)
- [var metaMethodNamesOffset: UInt32](./osclassdescription/api-3074895-metamethodnamesoffset.md)
- [var metaMethodNamesSize: UInt32](./osclassdescription/api-3074896-metamethodnamessize.md)
- [var metaMethodOptions: ()](./osclassdescription/api-3074897-metamethodoptions.md)
- [var metaMethodOptionsOffset: UInt32](./osclassdescription/api-3074898-metamethodoptionsoffset.md)
- [var metaMethodOptionsSize: UInt32](./osclassdescription/api-3074899-metamethodoptionssize.md)
- [var methodNames: ()](./osclassdescription/api-3074900-methodnames.md)
- [var methodNamesOffset: UInt32](./osclassdescription/api-3074901-methodnamesoffset.md)
- [var methodNamesSize: UInt32](./osclassdescription/api-3074902-methodnamessize.md)
- [var methodOptions: ()](./osclassdescription/api-3074903-methodoptions.md)
- [var methodOptionsOffset: UInt32](./osclassdescription/api-3074904-methodoptionsoffset.md)
- [var methodOptionsSize: UInt32](./osclassdescription/api-3074905-methodoptionssize.md)
- [var name: (CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar)](./osclassdescription/api-3074906-name.md)
- [var queueNamesOffset: UInt32](./osclassdescription/api-3074907-queuenamesoffset.md)
- [var queueNamesSize: UInt32](./osclassdescription/api-3074908-queuenamessize.md)
- [var resv1: (UInt64, UInt64, UInt64, UInt64, UInt64, UInt64, UInt64, UInt64)](./osclassdescription/api-3074909-resv1.md)
- [var superName: (CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar)](./osclassdescription/api-3074910-supername.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/osclassdescription)*