# Callback Constants for the AEResolve Function

**Framework**: Core Services

Specify supported callback features to the `AEResolve` function.

#### Overview

You use these constants to supply a value for the `callbackFlags` parameter to the [`AEResolve(_:_:_:)`](1449720-aeresolve.md) function. This value specifies whether your application supports whose descriptors or provides marking callback functions. To obtain a value for this parameter, you can add together constants to set the appropriate bits, as shown in the following example (for an application that supports both whose tests and marking):

```occ
    AEDesc objectSpecifier; // Previously obtained object specifier.     AEDesc  resultToken;
    OSErr myErr;
 
    myErr = AEResolve (&objectSpecifier,
                        kAEIDoWhose + kAEIDoMarking, &resultToken)
```

AppleScript generates whose clauses from script statements such as the following:

```occ
tell application "Finder"
    every file in control panels folder whose file type is "APPL"
end tell
```

## Topics

### Constants
- [var kAEIDoMinimum: Int](kaeidominimum.md)
  The application does not handle whose tests or provide marking callbacks.
- [var kAEIDoWhose: Int](kaeidowhose.md)
  The application supports whose tests (supports key form `formWhose`).
- [var kAEIDoMarking: Int](kaeidomarking.md)
  The application provides marking callback functions. Marking callback functions are described in [`Apple Event Manager`](https://developer.apple.com/documentation/applicationservices/apple_event_manager).
- [var kAEHandleSimpleRanges: Int](kaehandlesimpleranges.md)
- [var kAEPassSubDescs: Int](kaepasssubdescs.md)
- [var kAEResolveNestedLists: Int](kaeresolvenestedlists.md)
- [var kAEUseRelativeIterators: Int](kaeuserelativeiterators.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/apple_events/1572741-callback_constants_for_the_aeres)*