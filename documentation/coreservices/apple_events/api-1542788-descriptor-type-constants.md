# Descriptor Type Constants

**Framework**: Core Services

Specify types for descriptors.

#### Overview

The constants described here specify the data type for a descriptor and show the kind of data stored in a descriptor with that type.

Descriptors are the building blocks used by the Apple Event Manager to construct Apple event attributes and parameters. A descriptor is a data structure of type [`AEDesc`](aedesc.md), which consists of data storage and a descriptor type that identifies the type of the data. A descriptor type is defined by the data type [`DescType`](desctype.md). AppleScript defines descriptor type constants for a wide variety of common data types. For additional types, see [`Numeric Descriptor Type Constants`](apple_events/1542872-numeric_descriptor_type_constant.md) and [`Other Descriptor Type Constants`](apple_events/1542760-other_descriptor_type_constants.md). For a complete listing, including data types such as units of length, weight, and volume, see the Apple Event Manager and Open Scripting Architecture header files.

For the constant `typeApplicationURL`, the data that specifies the application URL takes the following format:

```occ
eppc://[username[:password]@]host/AppName[[?uid=#]&[pid=#]]
```

As indicated by this format:

- `username` is optional. If present, an `'@'` must appear before the host name. `password` is optional. If present, `username` is not optional, and the password must be separated from the username by a `':'` and must precede the `'@'`. `AppName` is not optional; if it contains non-UTF-8 characters or white space, it must be URL-encoded (for example, `My%20Application`).
- `uid` and `pid` are optional. If `pid` is present, `uid` and `AppName` are ignored and the event is delivered only to applications with the given process id. If `uid` is present, events are directed to the application name owned by the given user id.

The following are examples of valid URLs:

```occ
eppc://Steve%20Zellers:wombat@grrr.apple.com/Microsoft%20Word
eppc://Steve%20Zellers:wombat@grrr.apple.com/Microsoft%20Word?pid=1284
```

The availability of user identifiers provides enhanced Apple event support for Fast User Switching. Such identifiers make it possible to send Apple events to applications running in any session, if the uids of the processes match. `'root'` (or `uid 0`) processes are allowed to send Apple events to any process in any session. Non-root processes can only target applications that match their uid.

## Topics

### Constants
- [var typeAEList: DescType](typeaelist.md)
  List of descriptors.
- [var typeAERecord: DescType](typeaerecord.md)
  List of keyword-specified descriptors.
- [var typeAppleEvent: DescType](typeappleevent.md)
  Apple event.
- [var typeTrue: DescType](typetrue.md)
  `TRUE` Boolean value.
- [var typeFalse: DescType](typefalse.md)
  `FALSE` Boolean value.
- [var typeAlias: DescType](typealias.md)
  Alias.
- [var typeEnumerated: DescType](typeenumerated.md)
  Enumerated data.
- [var typeType: DescType](typetype.md)
  Four-character code for event class or event ID
- [var typeAppParameters: DescType](typeappparameters.md)
  Process Manager launch parameters.
- [var typeProperty: DescType](typeproperty.md)
  Apple event object property.
- [var typeFSRef: DescType](typefsref.md)
  File system reference. Use in preference to file system specifications (`typeFSS`).
- [var typeFileURL: DescType](typefileurl.md)
  A file URL. That is, the associated data consists of the bytes of a UTF-8 encoded URL with a scheme of "file". This type is appropriate for describing a file that may not yet exist—see [`Technical Note 2022`](https://developer.apple.comhttp://developer.apple.com/technotes/tn/tn2022.html) for more information.
- [var typeKeyword: DescType](typekeyword.md)
  Apple event keyword.
- [var typeSectionH: DescType](typesectionh.md)
  Handle to a section record. (Deprecated.)
- [var typeWildCard: DescType](typewildcard.md)
  Matches any type.
- [var typeApplSignature: DescType](typeapplsignature.md)
  Application signature.
- [var typeProcessSerialNumber: DescType](typeprocessserialnumber.md)
  A process serial number. See also [`AEAddressDesc`](aeaddressdesc.md).
- [var typeApplicationURL: DescType](typeapplicationurl.md)
  For specifying an application by URL. See Discussion section below for important information.
- [var typeNull: DescType](typenull.md)
  A null data storage pointer. When resolving an object specifier, an object with a null storage pointer specifies the default container at the top of the container hierarchy.
- [var typeBookmarkData: DescType](typebookmarkdata.md)
- [var typeEventRecord: DescType](typeeventrecord.md)
- [var typeFixed: DescType](typefixed.md)
- [var typeQDRectangle: DescType](typeqdrectangle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/apple_events/1542788-descriptor_type_constants)*