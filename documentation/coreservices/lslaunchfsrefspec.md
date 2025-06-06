# LSLaunchFSRefSpec

**Framework**: Core Services  
**Kind**: struct

The specification that defines, by file-system reference, an app to launch, items to open, or both, along with related information.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

## Declaration

```swift
struct LSLaunchFSRefSpec
```

#### Overview

This data type defines a file-based launch specification designating,by file-system reference, an application to launch, items to open,or both. To request that items be opened in a particular application,set `appRef`, `numDocs`,and `itemRefs` accordingly.To request that each designated item be opened in its own preferredapplication, set `appRef` to `NULL`. Torequest that a particular application be launched without openingany documents, set `appRef` accordinglyand set `numDocs` to `0`.

## Topics

### Initializers
- [init()](lslaunchfsrefspec/1443478-init.md)
- [init(appRef: UnsafePointer<FSRef>!, numDocs: Int, itemRefs: UnsafePointer<FSRef>!, passThruParams: UnsafePointer<AEDesc>!, launchFlags: LSLaunchFlags, asyncRefCon: UnsafeMutableRawPointer!)](lslaunchfsrefspec/1442457-init.md)
### Instance Properties
- [var appRef: UnsafePointer<FSRef>!](lslaunchfsrefspec/1448321-appref.md)
  A pointer to a file-system reference designatingthe application to launch; see the  inthe Carbon File Management Documentation for a description of the `FSRef` datatype. Set this field to `NULL` torequest that each item in the `itemRefs` arraybe opened in its own preferred application.
- [var asyncRefCon: UnsafeMutableRawPointer!](lslaunchfsrefspec/1450600-asyncrefcon.md)
  A pointer to an arbitrary application-definedvalue, passed in the Carbon event notifying you of an application’slaunch or termination (if you have registered for such notification).The value of this field can be `NULL`.
- [var itemRefs: UnsafePointer<FSRef>!](lslaunchfsrefspec/1444360-itemrefs.md)
  An array of file-system references designatingthe item or items to open. If the value of `numDocs` is `0`,this field is ignored and can be set to `NULL`.
- [var launchFlags: LSLaunchFlags](lslaunchfsrefspec/1449431-launchflags.md)
  Launch flags specifying how to launch each application(including whether to print or merely open documents); see [`LSLaunchFlags`](lslaunchflags.md) fora description of these flags.
- [var numDocs: Int](lslaunchfsrefspec/1450323-numdocs.md)
  The number of elements in the array specifiedby the `itemRefs` field.The value of this field can be `0`,in which case the application designated by `appRef` islaunched without opening any items.
- [var passThruParams: UnsafePointer<AEDesc>!](lslaunchfsrefspec/1445933-passthruparams.md)
  A pointer to an Apple event descriptor that ispassed untouched as an optional parameter, with keyword `keyAEPropData` (`'prdt'`),in the Apple event sent to each application launched or activated(whether individual preferred applications or the application designatedby `appRef`). See the  in the Carbon Interapplication CommunicationDocumentation for a description of the `AEDesc` datatype. The value of this field can be `NULL`.

## See Also

- [struct LSApplicationParameters](lsapplicationparameters.md)
  The specification that defines the app, launch flags, and additional parameters that control how an app launches.
- [struct LSItemInfoRecord](lsiteminforecord.md)
  The specification that contains requested information about an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec)*