# Apple Event Manager

**Framework**: Application Services

#### Overview

The Apple Event Manager, a part of the Open Scripting Architecture (OSA), provides facilities for applications to send and respond to Apple events and to make their operations and data available to AppleScript scripts. For related API reference, see Open Scripting Architecture Reference.

An Apple event is a type of interprocess message that can specify complex operations and data. Apple events provide a data transport and event dispatching mechanism  that can be used within a single application, between applications on the same computer, and between applications on different computers connected to a network.

Applications typically use Apple events to request services and information from other applications or to provide services and information in response to such requests. All applications that present a graphical interface to the user through the Human Interface Toolbox (Carbon applications) or the Cocoa application framework should be able to respond, if appropriate, to certain events sent by the Mac OS. These include the `open application` (or `launch`), `reopen`, `open documents`, `print documents`, and `quit` events.

Some Apple Event Manager functions are marked as being thread safe—for all other functions, you should call them only on the main thread.

For an overview of technologies that take advantage of the Apple Event Manager, see [`AppleScript Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/AppleScriptX.html#//apple_ref/doc/uid/10000156i).

For information on working with Apple events, including events sent by the Mac OS, see Responding to Apple Events in Apple Events Programming Guide. For information about individual four-character codes used in Apple events, see AppleScript Terminology and Apple Event Codes Reference.

The Apple Event Manager is implemented by the AE framework, a subframework of the Core Services framework. You don’t link directly with the AE framework—instead, you typically link with  the Carbon framework, which includes it. Some AppleEvent definitions are only available to clients of the Carbon framework, which includes, for example, `AEInteraction.h` in the HIToolbox framework.

The AE framework does not force a connection to the window server. This allows daemons and startup items that work with Apple events to continue working across log outs.

##### 1770164

You can check for version and feature availabilityinformation by using the Apple Event Manager selectors defined inthe Gestalt Manager. For more information see . 

## Topics

### Adding Items to Descriptor Lists
- [func AEPutArray(UnsafeMutablePointer<AEDescList>!, AEArrayType, UnsafePointer<AEArrayData>!, DescType, Size, Int) -> OSErr](../coreservices/1442535-aeputarray.md)
  Inserts the data for an Apple event array into a descriptor list, replacing any previous descriptors in the list.
- [func AEPutDesc(UnsafeMutablePointer<AEDescList>!, Int, UnsafePointer<AEDesc>!) -> OSErr](../coreservices/1450093-aeputdesc.md)
  Adds a descriptor to any descriptor list, possibly replacing an existing descriptor in the list.
- [func AEPutPtr(UnsafeMutablePointer<AEDescList>!, Int, DescType, UnsafeRawPointer!, Size) -> OSErr](../coreservices/1445287-aeputptr.md)
  Inserts data specified in a buffer into a descriptor list as a descriptor, possibly replacing an existing descriptor in the list.
### Adding Parameters and Attributes to Apple Events and Apple Event Records
- [func AEPutAttributeDesc(UnsafeMutablePointer<AppleEvent>!, AEKeyword, UnsafePointer<AEDesc>!) -> OSErr](../coreservices/1441790-aeputattributedesc.md)
  Adds a descriptor and a keyword to an Apple event as an attribute.
- [func AEPutAttributePtr(UnsafeMutablePointer<AppleEvent>!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSErr](../coreservices/1445940-aeputattributeptr.md)
  Adds a pointer to data, a descriptor type, and a keyword to an Apple event as an attribute.
- [func AEPutParamDesc(UnsafeMutablePointer<AppleEvent>!, AEKeyword, UnsafePointer<AEDesc>!) -> OSErr](../coreservices/1447576-aeputparamdesc.md)
  Inserts a descriptor and a keyword into an Apple event or Apple event record as an Apple event parameter.
- [func AEPutParamPtr(UnsafeMutablePointer<AppleEvent>!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSErr](../coreservices/1449263-aeputparamptr.md)
  Inserts data, a descriptor type, and a keyword into an Apple event or Apple event record as an Apple event parameter.
### Coercing Descriptor Types
- [func AECoerceDesc(UnsafePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1446519-aecoercedesc.md)
  Coerces the data in a descriptor to another descriptor type and creates a descriptor containing the newly coerced data.
- [func AECoercePtr(DescType, UnsafeRawPointer!, Size, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1441846-aecoerceptr.md)
  Coerces data to a desired descriptor type and creates a descriptor containing the newly coerced data.
### Counting the Items in Descriptor Lists
- [func AECountItems(UnsafePointer<AEDescList>!, UnsafeMutablePointer<Int>!) -> OSErr](../coreservices/1449533-aecountitems.md)
  Counts the number of descriptors in a descriptor list.
### Creating an Apple Event
- [func AECreateAppleEvent(AEEventClass, AEEventID, UnsafePointer<AEAddressDesc>!, AEReturnID, AETransactionID, UnsafeMutablePointer<AppleEvent>!) -> OSErr](../coreservices/1448525-aecreateappleevent.md)
  Creates an Apple event with several important attributes but no parameters.
### Creating and Duplicating Descriptors
- [func AECreateDesc(DescType, UnsafeRawPointer!, Size, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1448535-aecreatedesc.md)
  Creates a new descriptor that incorporates the specified data.
- [func AECreateDescFromExternalPtr(OSType, UnsafeRawPointer!, Size, AEDisposeExternalUPP!, SRefCon!, UnsafeMutablePointer<AEDesc>!) -> OSStatus](../coreservices/1446239-aecreatedescfromexternalptr.md)
  Creates a new descriptor that uses a memory buffer supplied by the caller.
- [func AEDuplicateDesc(UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1442661-aeduplicatedesc.md)
  Creates a copy of a descriptor.
### Creating, Calling, and Deleting Universal Procedure Pointers
- [func DisposeAECoerceDescUPP(AECoerceDescUPP!)](../coreservices/1448721-disposeaecoercedescupp.md)
  Disposes of a universal procedure pointer to a function that coerces data stored in a descriptor.
- [func DisposeAECoercePtrUPP(AECoercePtrUPP!)](../coreservices/1450664-disposeaecoerceptrupp.md)
  Disposes of a universal procedure pointer to a function that coerces data stored in a buffer.
- [func DisposeAEDisposeExternalUPP(AEDisposeExternalUPP!)](../coreservices/1447284-disposeaedisposeexternalupp.md)
  Disposes of a universal procedure pointer to a function that disposes of data supplied to the `AECreateDescFromExternalPtr` function.
- [func DisposeAEEventHandlerUPP(AEEventHandlerUPP!)](../coreservices/1442066-disposeaeeventhandlerupp.md)
  Disposes of a universal procedure pointer to an event handler function.
- [func DisposeOSLAccessorUPP(OSLAccessorUPP!)](../coreservices/1444684-disposeoslaccessorupp.md)
  Disposes of a universal procedure pointer to an object accessor function.
- [func DisposeOSLAdjustMarksUPP(OSLAdjustMarksUPP!)](../coreservices/1443940-disposeosladjustmarksupp.md)
  Disposes of a universal procedure pointer to an object callback adjust marks function.
- [func DisposeOSLCompareUPP(OSLCompareUPP!)](../coreservices/1448398-disposeoslcompareupp.md)
  Disposes of a universal procedure pointer to an object callback comparison function.
- [func DisposeOSLCountUPP(OSLCountUPP!)](../coreservices/1443984-disposeoslcountupp.md)
  Disposes of a universal procedure pointer to an object callback count function.
- [func DisposeOSLDisposeTokenUPP(OSLDisposeTokenUPP!)](../coreservices/1442670-disposeosldisposetokenupp.md)
  Disposes of a universal procedure pointer to an object callback dispose token function.
- [func DisposeOSLGetErrDescUPP(OSLGetErrDescUPP!)](../coreservices/1446061-disposeoslgeterrdescupp.md)
  Disposes of a universal procedure pointer to an object callback get error descriptor function.
- [func DisposeOSLGetMarkTokenUPP(OSLGetMarkTokenUPP!)](../coreservices/1442377-disposeoslgetmarktokenupp.md)
  Disposes of a universal procedure pointer to an object callback get mark function.
- [func DisposeOSLMarkUPP(OSLMarkUPP!)](../coreservices/1449253-disposeoslmarkupp.md)
  Disposes of a universal procedure pointer to an object callback mark function.
- [func InvokeAECoerceDescUPP(UnsafePointer<AEDesc>!, DescType, SRefCon!, UnsafeMutablePointer<AEDesc>!, AECoerceDescUPP!) -> OSErr](../coreservices/1445450-invokeaecoercedescupp.md)
  Calls a universal procedure pointer to a function that coerces data stored in a descriptor.
- [func InvokeAECoercePtrUPP(DescType, UnsafeRawPointer!, Size, DescType, SRefCon!, UnsafeMutablePointer<AEDesc>!, AECoercePtrUPP!) -> OSErr](../coreservices/1447079-invokeaecoerceptrupp.md)
  Calls a universal procedure pointer to a function that coerces data stored in a buffer.
- [func InvokeAEDisposeExternalUPP(UnsafeRawPointer!, Size, SRefCon!, AEDisposeExternalUPP!)](../coreservices/1441717-invokeaedisposeexternalupp.md)
  Calls a dispose external universal procedure pointer.
- [func InvokeAEEventHandlerUPP(UnsafePointer<AppleEvent>!, UnsafeMutablePointer<AppleEvent>!, SRefCon!, AEEventHandlerUPP!) -> OSErr](../coreservices/1446585-invokeaeeventhandlerupp.md)
  Calls an event handler universal procedure pointer.
- [func InvokeOSLAccessorUPP(DescType, UnsafePointer<AEDesc>!, DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, SRefCon!, OSLAccessorUPP!) -> OSErr](../coreservices/1448978-invokeoslaccessorupp.md)
  Calls an object accessor universal procedure pointer.
- [func InvokeOSLAdjustMarksUPP(Int, Int, UnsafePointer<AEDesc>!, OSLAdjustMarksUPP!) -> OSErr](../coreservices/1448506-invokeosladjustmarksupp.md)
  Calls an object callback adjust marks universal procedure pointer.
- [func InvokeOSLCompareUPP(DescType, UnsafePointer<AEDesc>!, UnsafePointer<AEDesc>!, UnsafeMutablePointer<DarwinBoolean>!, OSLCompareUPP!) -> OSErr](../coreservices/1443110-invokeoslcompareupp.md)
  Calls an object callback comparison universal procedure pointer.
- [func InvokeOSLCountUPP(DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<Int>!, OSLCountUPP!) -> OSErr](../coreservices/1448030-invokeoslcountupp.md)
  Calls an object callback count universal procedure pointer.
- [func InvokeOSLDisposeTokenUPP(UnsafeMutablePointer<AEDesc>!, OSLDisposeTokenUPP!) -> OSErr](../coreservices/1443963-invokeosldisposetokenupp.md)
  Calls an object callback dispose token universal procedure pointer.
- [func InvokeOSLGetErrDescUPP(UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>?>!, OSLGetErrDescUPP!) -> OSErr](../coreservices/1448420-invokeoslgeterrdescupp.md)
  Calls an object callback get error descriptor universal procedure pointer.
- [func InvokeOSLGetMarkTokenUPP(UnsafePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!, OSLGetMarkTokenUPP!) -> OSErr](../coreservices/1441894-invokeoslgetmarktokenupp.md)
  Calls an object callback get mark universal procedure pointer.
- [func InvokeOSLMarkUPP(UnsafePointer<AEDesc>!, UnsafePointer<AEDesc>!, Int, OSLMarkUPP!) -> OSErr](../coreservices/1447444-invokeoslmarkupp.md)
  Calls an object callback mark universal procedure pointer.
- [func NewAECoerceDescUPP(AECoerceDescProcPtr!) -> AECoerceDescUPP!](../coreservices/1445885-newaecoercedescupp.md)
  Creates a new universal procedure pointer to a function that coerces data stored in a descriptor.
- [func NewAECoercePtrUPP(AECoercePtrProcPtr!) -> AECoercePtrUPP!](../coreservices/1449962-newaecoerceptrupp.md)
  Creates a new universal procedure pointer to a function that coerces data stored in a buffer.
- [func NewAEDisposeExternalUPP(AEDisposeExternalProcPtr!) -> AEDisposeExternalUPP!](../coreservices/1447774-newaedisposeexternalupp.md)
  Creates a new universal procedure pointer to a function that disposes of data stored in a buffer.
- [func NewAEEventHandlerUPP(AEEventHandlerProcPtr!) -> AEEventHandlerUPP!](../coreservices/1446862-newaeeventhandlerupp.md)
  Creates a new universal procedure pointer to an event handler function.
- [func NewOSLAccessorUPP(OSLAccessorProcPtr!) -> OSLAccessorUPP!](../coreservices/1449584-newoslaccessorupp.md)
  Creates a new universal procedure pointer to an object accessor function.
- [func NewOSLAdjustMarksUPP(OSLAdjustMarksProcPtr!) -> OSLAdjustMarksUPP!](../coreservices/1443347-newosladjustmarksupp.md)
  Creates a new universal procedure pointer to an object callback adjust marks function.
- [func NewOSLCompareUPP(OSLCompareProcPtr!) -> OSLCompareUPP!](../coreservices/1444603-newoslcompareupp.md)
  Creates a new universal procedure pointer to an object callback comparison function.
- [func NewOSLCountUPP(OSLCountProcPtr!) -> OSLCountUPP!](../coreservices/1448156-newoslcountupp.md)
  Creates a new universal procedure pointer to an object callback count function.
- [func NewOSLDisposeTokenUPP(OSLDisposeTokenProcPtr!) -> OSLDisposeTokenUPP!](../coreservices/1450027-newosldisposetokenupp.md)
  Creates a new universal procedure pointer to an object callback dispose token function.
- [func NewOSLGetErrDescUPP(OSLGetErrDescProcPtr!) -> OSLGetErrDescUPP!](../coreservices/1447934-newoslgeterrdescupp.md)
  Creates a new universal procedure pointer to an object callback get error descriptor function.
- [func NewOSLGetMarkTokenUPP(OSLGetMarkTokenProcPtr!) -> OSLGetMarkTokenUPP!](../coreservices/1445166-newoslgetmarktokenupp.md)
  Creates a new universal procedure pointer to an object callback get mark function.
- [func NewOSLMarkUPP(OSLMarkProcPtr!) -> OSLMarkUPP!](../coreservices/1446942-newoslmarkupp.md)
  Creates a new universal procedure pointer to an object callback mark function.
### Creating Descriptor Lists and Apple Event Records
- [func AECreateList(UnsafeRawPointer!, Size, Bool, UnsafeMutablePointer<AEDescList>!) -> OSErr](../coreservices/1448643-aecreatelist.md)
  Creates an empty descriptor list or Apple event record.
### Creating Object Specifiers
- [func CreateCompDescriptor(DescType, UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1449155-createcompdescriptor.md)
  Creates a comparison descriptor that specifies how to compare one or more Apple event objects with either another Apple event object or a descriptor.
- [func CreateLogicalDescriptor(UnsafeMutablePointer<AEDescList>!, DescType, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1445212-createlogicaldescriptor.md)
  Creates a logical descriptor that specifies a logical operator and one or more logical terms for the Apple Event Manager to evaluate. 
- [func CreateObjSpecifier(DescType, UnsafeMutablePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1450244-createobjspecifier.md)
  Assembles an object specifier that identifies one or more Apple event objects, from other descriptors.
- [func CreateOffsetDescriptor(Int, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1444957-createoffsetdescriptor.md)
  Creates an offset descriptor that specifies the position of an element in relation to the beginning or end of its container. 
- [func CreateRangeDescriptor(UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1444087-createrangedescriptor.md)
  Creates a range descriptor that specifies a series of consecutive elements in the same container. 
### Deallocating Memory for Descriptors
- [func AEDisposeDesc(UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1444208-aedisposedesc.md)
  Deallocates the memory used by a descriptor.
### Deallocating Memory for Tokens
- [func AEDisposeToken(UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1446783-aedisposetoken.md)
  Deallocates the memory used by a token.
### Deleting Descriptors
- [func AEDeleteItem(UnsafeMutablePointer<AEDescList>!, Int) -> OSErr](../coreservices/1447164-aedeleteitem.md)
  Deletes a descriptor from a descriptor list, causing all subsequent descriptors to move up one place. 
- [func AEDeleteParam(UnsafeMutablePointer<AppleEvent>!, AEKeyword) -> OSErr](../coreservices/1444338-aedeleteparam.md)
  Deletes a keyword-specified parameter from an Apple event record.
### Getting, Calling, and Removing Object Accessor Functions
- [func AECallObjectAccessor(DescType, UnsafePointer<AEDesc>!, DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1447059-aecallobjectaccessor.md)
  Invokes the appropriate object accessor function for a specific desired type and container type. 
- [func AEGetObjectAccessor(DescType, DescType, UnsafeMutablePointer<OSLAccessorUPP?>!, UnsafeMutablePointer<SRefCon?>!, Bool) -> OSErr](../coreservices/1449054-aegetobjectaccessor.md)
  Gets an object accessor function from an object accessor dispatch table. 
- [func AEInstallObjectAccessor(DescType, DescType, OSLAccessorUPP!, SRefCon!, Bool) -> OSErr](../coreservices/1447905-aeinstallobjectaccessor.md)
  Adds or replaces an entry for an object accessor function to an object accessor dispatch table.
- [func AERemoveObjectAccessor(DescType, DescType, OSLAccessorUPP!, Bool) -> OSErr](../coreservices/1442552-aeremoveobjectaccessor.md)
  Removes an object accessor function from an object accessor dispatch table. 
### Getting Data or Descriptors From Apple Events and Apple Event Records
- [func AEGetAttributeDesc(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1450314-aegetattributedesc.md)
  Gets a copy of the descriptor for a specified Apple event attribute from an Apple event; typically used when your application needs to pass the descriptor on to another function.
- [func AEGetAttributePtr(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](../coreservices/1445109-aegetattributeptr.md)
  Gets a copy of the data for a specified Apple event attribute from an Apple event; typically used when your application needs to work with the data directly.
- [func AEGetParamDesc(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1449233-aegetparamdesc.md)
  Gets a copy of the descriptor for a keyword-specified Apple event parameter from an Apple event or an Apple event record.
- [func AEGetParamPtr(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](../coreservices/1444069-aegetparamptr.md)
  Gets a copy of the data for a specified Apple event parameter from an Apple event or an Apple event record.
### Getting Information About the Apple Event Manager
- [func AEManagerInfo(AEKeyword, UnsafeMutablePointer<Int>!) -> OSErr](../coreservices/1449373-aemanagerinfo.md)
  Provides information about the version of the Apple Event Manager currently available or the number of processes that are currently recording Apple events.
### Getting Items From Descriptor Lists
- [func AEGetArray(UnsafePointer<AEDescList>!, AEArrayType, AEArrayDataPointer!, Size, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!, UnsafeMutablePointer<Int>!) -> OSErr](../coreservices/1445720-aegetarray.md)
  Extracts data from an Apple event array created with the `AEPutArray` function and stores it as a standard array of fixed size items in the specified buffer.
- [func AEGetNthDesc(UnsafePointer<AEDescList>!, Int, DescType, UnsafeMutablePointer<AEKeyword>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1448326-aegetnthdesc.md)
   Copies a descriptor from a specified position in a descriptor list into a specified descriptor; typically used when your application needs to pass the extracted data to another function as a descriptor.
- [func AEGetNthPtr(UnsafePointer<AEDescList>!, Int, DescType, UnsafeMutablePointer<AEKeyword>!, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](../coreservices/1447539-aegetnthptr.md)
  Gets a copy of the data from a descriptor at a specified position in a descriptor list; typically used when your application needs to work with the extracted data directly.
### Getting the Sizes and Descriptor Types of Descriptors
- [func AESizeOfAttribute(UnsafePointer<AppleEvent>!, AEKeyword, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](../coreservices/1445764-aesizeofattribute.md)
  Gets the size and descriptor type of an Apple event attribute from a descriptor of type `AppleEvent`.
- [func AESizeOfNthItem(UnsafePointer<AEDescList>!, Int, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](../coreservices/1447307-aesizeofnthitem.md)
  Gets the data size and descriptor type of the descriptor at a specified position in a descriptor list.
- [func AESizeOfParam(UnsafePointer<AppleEvent>!, AEKeyword, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](../coreservices/1449998-aesizeofparam.md)
  Gets the size and descriptor type of an Apple event parameter from a descriptor of type `AERecord` or `AppleEvent`.
### Initializing the Object Support Library
- [func AEObjectInit() -> OSErr](../coreservices/1447372-aeobjectinit.md)
  Initializes the Object Support Library.
- [func AESetObjectCallbacks(OSLCompareUPP!, OSLCountUPP!, OSLDisposeTokenUPP!, OSLGetMarkTokenUPP!, OSLMarkUPP!, OSLAdjustMarksUPP!, OSLGetErrDescUPP!) -> OSErr](../coreservices/1447756-aesetobjectcallbacks.md)
  Specifies the object callback functions for your application.
### Locating Processes on Remote Computers
- [func AECreateRemoteProcessResolver(CFAllocator!, CFURL!) -> AERemoteProcessResolverRef!](../coreservices/1445692-aecreateremoteprocessresolver.md)
  Creates an object for resolving a list of remote processes.
- [func AEDisposeRemoteProcessResolver(AERemoteProcessResolverRef!)](../coreservices/1442572-aedisposeremoteprocessresolver.md)
  Disposes of an `AERemoteProcessResolverRef`.
- [func AERemoteProcessResolverGetProcesses(AERemoteProcessResolverRef!, UnsafeMutablePointer<CFStreamError>!) -> Unmanaged<CFArray>!](../coreservices/1444456-aeremoteprocessresolvergetproces.md)
  Returns an array of objects containing information about processes running on a remote machine.
- [func AERemoteProcessResolverScheduleWithRunLoop(AERemoteProcessResolverRef!, CFRunLoop!, CFString!, AERemoteProcessResolverCallback!, UnsafePointer<AERemoteProcessResolverContext>!)](../coreservices/1447259-aeremoteprocessresolverschedulew.md)
  Schedules a resolver for execution on a given run loop in a given mode.
### Managing Apple Event Dispatch Tables
- [func AEGetEventHandler(AEEventClass, AEEventID, UnsafeMutablePointer<AEEventHandlerUPP?>!, UnsafeMutablePointer<SRefCon?>!, Bool) -> OSErr](../coreservices/1445631-aegeteventhandler.md)
  Gets an event handler from an Apple event dispatch table.
- [func AEInstallEventHandler(AEEventClass, AEEventID, AEEventHandlerUPP!, SRefCon!, Bool) -> OSErr](../coreservices/1448596-aeinstalleventhandler.md)
  Adds an entry for an event handler to an Apple event dispatch table.
- [func AERemoveEventHandler(AEEventClass, AEEventID, AEEventHandlerUPP!, Bool) -> OSErr](../coreservices/1445239-aeremoveeventhandler.md)
  Removes an event handler entry from an Apple event dispatch table.
### Managing Coercion Handler Dispatch Tables
- [func AEGetCoercionHandler(DescType, DescType, UnsafeMutablePointer<AECoercionHandlerUPP?>!, UnsafeMutablePointer<SRefCon?>!, UnsafeMutablePointer<DarwinBoolean>!, Bool) -> OSErr](../coreservices/1445348-aegetcoercionhandler.md)
  Gets the coercion handler for a specified descriptor type.
- [func AEInstallCoercionHandler(DescType, DescType, AECoercionHandlerUPP!, SRefCon!, Bool, Bool) -> OSErr](../coreservices/1445548-aeinstallcoercionhandler.md)
  Installs a coercion handler in either the application or system coercion handler dispatch table.
- [func AERemoveCoercionHandler(DescType, DescType, AECoercionHandlerUPP!, Bool) -> OSErr](../coreservices/1441907-aeremovecoercionhandler.md)
  Removes a coercion handler from a coercion handler dispatch table.
### Managing Special Handler Dispatch Tables
- [func AEGetSpecialHandler(AEKeyword, UnsafeMutablePointer<AEEventHandlerUPP?>!, Bool) -> OSErr](../coreservices/1444274-aegetspecialhandler.md)
  Gets a specified handler from a special handler dispatch table.
- [func AEInstallSpecialHandler(AEKeyword, AEEventHandlerUPP!, Bool) -> OSErr](../coreservices/1445532-aeinstallspecialhandler.md)
  Installs a callback function in a special handler dispatch table.
- [func AERemoveSpecialHandler(AEKeyword, AEEventHandlerUPP!, Bool) -> OSErr](../coreservices/1447960-aeremovespecialhandler.md)
  Removes a handler from a special handler dispatch table.
### Operating On Descriptor Data
- [func AEGetDescData(UnsafePointer<AEDesc>!, UnsafeMutableRawPointer!, Size) -> OSErr](../coreservices/1444427-aegetdescdata.md)
  Gets the data from the specified descriptor.
- [func AEGetDescDataSize(UnsafePointer<AEDesc>!) -> Size](../coreservices/1450119-aegetdescdatasize.md)
  Gets the size, in bytes, of the data in the specified descriptor.
- [func AEGetDescDataRange(UnsafePointer<AEDesc>!, UnsafeMutableRawPointer!, Size, Size) -> OSStatus](../coreservices/1446560-aegetdescdatarange.md)
  Retrieves a specified series of bytes from the specified descriptor.
- [func AEReplaceDescData(DescType, UnsafeRawPointer!, Size, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1446695-aereplacedescdata.md)
  Copies the specified data into the specified descriptor, replacing any previous data.
### Resolving Object Specifiers
- [func AEResolve(UnsafePointer<AEDesc>!, Int16, UnsafeMutablePointer<AEDesc>!) -> OSErr](../coreservices/1449720-aeresolve.md)
  Resolves an object specifier.
### Creating Apple Event Structures in Memory
- [func AEPrintDescToHandle(UnsafePointer<AEDesc>!, UnsafeMutablePointer<Handle?>!) -> OSStatus](../coreservices/1445158-aeprintdesctohandle.md)
  Provides a pretty printer facility for displaying the contents of Apple event descriptors.
- [func vAEBuildAppleEvent(AEEventClass, AEEventID, DescType, UnsafeRawPointer!, Size, Int16, Int32, UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](../coreservices/1441729-vaebuildappleevent.md)
  Allows you to encapsulate calls to `AEBuildAppleEvent` in a wrapper routine.
- [func vAEBuildDesc(UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](../coreservices/1446775-vaebuilddesc.md)
  Allows you to encapsulate calls to `AEBuildDesc` in your own wrapper routines.
- [func vAEBuildParameters(UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](../coreservices/1448040-vaebuildparameters.md)
  Allows you to encapsulate calls to `AEBuildParameters` in your own `stdarg`-style wrapper routines, using techniques similar to those allowed by vsprintf.
### Creating Apple Event Structures Using Streams
- [func AEStreamClose(AEStreamRef!, UnsafeMutablePointer<AEDesc>!) -> OSStatus](../coreservices/1449821-aestreamclose.md)
  Closes and deallocates an `AEStreamRef`.
- [func AEStreamCloseDesc(AEStreamRef!) -> OSStatus](../coreservices/1449272-aestreamclosedesc.md)
  Marks the end of a descriptor in an `AEStreamRef`.
- [func AEStreamCloseList(AEStreamRef!) -> OSStatus](../coreservices/1448185-aestreamcloselist.md)
  Marks the end of a list of descriptors in an `AEStreamRef`.
- [func AEStreamCloseRecord(AEStreamRef!) -> OSStatus](../coreservices/1449522-aestreamcloserecord.md)
  Marks the end of a record in an `AEStreamRef`.
- [func AEStreamCreateEvent(AEEventClass, AEEventID, DescType, UnsafeRawPointer!, Size, Int16, Int32) -> AEStreamRef!](../coreservices/1446562-aestreamcreateevent.md)
  Creates a new Apple event and opens a stream for writing data to it.
- [func AEStreamOpen() -> AEStreamRef!](../coreservices/1447732-aestreamopen.md)
  Opens a new `AEStreamRef` for use in building a descriptor.
- [func AEStreamOpenDesc(AEStreamRef!, DescType) -> OSStatus](../coreservices/1446544-aestreamopendesc.md)
  Marks the beginning of a descriptor in an `AEStreamRef`.
- [func AEStreamOpenEvent(UnsafeMutablePointer<AppleEvent>!) -> AEStreamRef!](../coreservices/1445366-aestreamopenevent.md)
  Opens a stream for an existing Apple event.
- [func AEStreamOpenKeyDesc(AEStreamRef!, AEKeyword, DescType) -> OSStatus](../coreservices/1442897-aestreamopenkeydesc.md)
  Marks the beginning of a key descriptor in an `AEStreamRef`.
- [func AEStreamOpenList(AEStreamRef!) -> OSStatus](../coreservices/1448594-aestreamopenlist.md)
  Marks the beginning of a descriptor list in an `AEStreamRef`.
- [func AEStreamOpenRecord(AEStreamRef!, DescType) -> OSStatus](../coreservices/1447141-aestreamopenrecord.md)
  Marks the beginning of an Apple event record in an `AEStreamRef`.
- [func AEStreamOptionalParam(AEStreamRef!, AEKeyword) -> OSStatus](../coreservices/1444481-aestreamoptionalparam.md)
  Designates a parameter in an Apple event as optional.
- [func AEStreamSetRecordType(AEStreamRef!, DescType) -> OSStatus](../coreservices/1447704-aestreamsetrecordtype.md)
  Sets the type of the most recently created record in an `AEStreamRef`.
- [func AEStreamWriteAEDesc(AEStreamRef!, UnsafePointer<AEDesc>!) -> OSStatus](../coreservices/1448487-aestreamwriteaedesc.md)
  Copies an existing descriptor into an `AEStreamRef`.
- [func AEStreamWriteData(AEStreamRef!, UnsafeRawPointer!, Size) -> OSStatus](../coreservices/1442610-aestreamwritedata.md)
  Appends data to the current descriptor in an `AEStreamRef`.
- [func AEStreamWriteDesc(AEStreamRef!, DescType, UnsafeRawPointer!, Size) -> OSStatus](../coreservices/1450387-aestreamwritedesc.md)
  Appends the data for a complete descriptor to an `AEStreamRef`.
- [func AEStreamWriteKey(AEStreamRef!, AEKeyword) -> OSStatus](../coreservices/1448750-aestreamwritekey.md)
  Marks the beginning of a keyword/descriptor pair for a descriptor in an `AEStreamRef`.
- [func AEStreamWriteKeyDesc(AEStreamRef!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSStatus](../coreservices/1442568-aestreamwritekeydesc.md)
  Writes a complete keyword/descriptor pair to an `AEStreamRef`.
### Working With Lower Level Apple Event Functions
- [func AEGetRegisteredMachPort() -> mach_port_t](../coreservices/1449736-aegetregisteredmachport.md)
  Returns the Mach port (in the form of a `mach_port_t`) that was registered with the bootstrap server for this process.
- [func AEDecodeMessage(UnsafeMutablePointer<mach_msg_header_t>!, UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AppleEvent>!) -> OSStatus](../coreservices/1447827-aedecodemessage.md)
  Decodes a Mach message and converts it into an Apple event and its related reply.
- [func AESendMessage(UnsafePointer<AppleEvent>!, UnsafeMutablePointer<AppleEvent>!, AESendMode, Int) -> OSStatus](../coreservices/1442994-aesendmessage.md)
  Sends an AppleEvent to a target process without some of the overhead required by `AESend`.
- [func AEProcessMessage(UnsafeMutablePointer<mach_msg_header_t>!) -> OSStatus](../coreservices/1444387-aeprocessmessage.md)
  Decodes and dispatches a low level Mach message event to an event handler, including packaging and returning the reply to the sender.
### Serializing Apple Event Data
- [func AESizeOfFlattenedDesc(UnsafePointer<AEDesc>!) -> Size](../coreservices/1447305-aesizeofflatteneddesc.md)
  Returns the amount of buffer space needed to store the descriptor after flattening it.
- [func AEFlattenDesc(UnsafePointer<AEDesc>!, Ptr!, Size, UnsafeMutablePointer<Size>!) -> OSStatus](../coreservices/1441808-aeflattendesc.md)
  Flattens the specified descriptor and stores the data in the supplied buffer.
- [func AEUnflattenDesc(UnsafeRawPointer!, UnsafeMutablePointer<AEDesc>!) -> OSStatus](../coreservices/1448997-aeunflattendesc.md)
  Unflattens the data in the passed buffer and creates a descriptor from it.
### Miscellaneous
- [func AECheckIsRecord(UnsafePointer<AEDesc>!) -> Bool](../coreservices/1444011-aecheckisrecord.md)
  Determines whether a descriptor is truly an `AERecord`.
- [func AEInitializeDesc(UnsafeMutablePointer<AEDesc>!)](../coreservices/1446047-aeinitializedesc.md)
  Initializes a new descriptor. 
### Callbacks
- [typealias AERemoteProcessResolverCallback](../coreservices/aeremoteprocessresolvercallback.md)
  Defines a pointer to a function the Apple Event Manager calls when the asynchronous execution of a remote process resolver completes, either due to success or failure, after a call to the `AERemoteProcessResolverScheduleWithRunLoop` function. Your callback function can use the reference passed to it to get the remote process information.
- [typealias AEDisposeExternalProcPtr](../coreservices/aedisposeexternalprocptr.md)
  Defines a pointer to a function the Apple Event Manager calls to dispose of a descriptor created by the `AECreateDescFromExternalPtr` function. Your callback function disposes of the buffer you originally passed to that function.
- [typealias AECoerceDescProcPtr](../coreservices/aecoercedescprocptr.md)
  Defines a pointer to a function that coerces data stored in a descriptor. Your descriptor coercion callback function coerces the data from the passed descriptor to the specified type, returning the coerced data in a second descriptor.
- [typealias AECoercePtrProcPtr](../coreservices/aecoerceptrprocptr.md)
  Defines a pointer to a function that coerces data stored in a buffer. Your pointer coercion callback routine coerces the data from the passed buffer to the specified type, returning the coerced data in a descriptor.
- [typealias AEEventHandlerProcPtr](../coreservices/aeeventhandlerprocptr.md)
  Defines a pointer to a function that handles one or more Apple events. Your Apple event handler function performs any action requested by the Apple event, adds parameters to the reply Apple event if appropriate (possibly including error information), and returns a result code.
- [typealias OSLAccessorProcPtr](../coreservices/oslaccessorprocptr.md)
  Your object accessor function either finds elements or properties of an Apple event object.
- [typealias OSLAdjustMarksProcPtr](../coreservices/osladjustmarksprocptr.md)
  Defines a pointer to an adjust marks callback function. Your adjust marks function unmarks objects previously marked by a call to your marking function.
- [typealias OSLCompareProcPtr](../coreservices/oslcompareprocptr.md)
  Defines a pointer to an object comparison callback function. Your object comparison function compares one Apple event object to another or to the data for a descriptor.
- [typealias OSLCountProcPtr](../coreservices/oslcountprocptr.md)
  Defines a pointer to an object counting callback function. Your object counting function counts the number of Apple event objects of a specified class in a specified container object.
- [typealias OSLDisposeTokenProcPtr](../coreservices/osldisposetokenprocptr.md)
  Defines a pointer to a dispose token callback function. Your dispose token function, required only if you use a complex token format, disposes of the specified token.
- [typealias OSLGetErrDescProcPtr](../coreservices/oslgeterrdescprocptr.md)
  Defines a pointer to an error descriptor callback function. Your error descriptor callback function supplies a pointer to an address where the Apple Event Manager can store the current descriptor if an error occurs during a call to the `AEResolve` function.
- [typealias OSLGetMarkTokenProcPtr](../coreservices/oslgetmarktokenprocptr.md)
  Defines a pointer to a mark token callback function. Your mark token function returns a mark token.
- [typealias OSLMarkProcPtr](../coreservices/oslmarkprocptr.md)
  Defines a pointer to an object marking callback function. Your object-marking function marks a specific Apple event object.
### Data Types
- [struct AEArrayData](../coreservices/aearraydata.md)
  Stores array information to be put into a descriptor listwith the `AEPutArray` functionor extracted from a descriptor list with the `AEGetArray` function.
- [struct AEBuildError](../coreservices/aebuilderror.md)
  Defines a structure for storing additional error codeinformation for “AEBuild” routines.
- [struct AEDesc](../coreservices/aedesc.md)
  Stores data and an accompanying descriptor type to formthe basic building block of all Apple Events.
- [struct AEKeyDesc](../coreservices/aekeydesc.md)
  Associates a keyword with a descriptor to form a keyword-specifieddescriptor.
- [struct AERemoteProcessResolverContext](../coreservices/aeremoteprocessresolvercontext.md)
  Supplied as a parameter when performing asynchronous resolutionof remote processes.
- [struct ccntTokenRecord](../coreservices/ccnttokenrecord.md)
  Stores token information used by the AEResolve functionwhile locating a range of objects.
- [struct IntlText](../coreservices/intltext.md)
  International text consists of an ordered series of bytes, beginning with a 4-byte language code and a 4-byte script code that together determine the format of the bytes that follow.
- [struct OffsetArray](../coreservices/offsetarray.md)
  Specifies offsets of ranges of text. Not typically used by developers.
- [struct TextRange](../coreservices/textrange.md)
  Specifies a range of text. Not typically used by developers.
- [struct TextRangeArray](../coreservices/textrangearray.md)
  Specifies an array of text ranges. Not typically used by developers.
- [struct TScriptingSizeResource](../coreservices/tscriptingsizeresource.md)
  Defines a data type to store stack and heap information. Not typically used by developers.
- [struct WritingCode](../coreservices/writingcode.md)
- [typealias AEAddressDesc](../coreservices/aeaddressdesc.md)
  A descriptor that contains the address of an application, used to describe the target application for an Apple event.
- [typealias AEArrayDataPointer](../coreservices/aearraydatapointer.md)
  A pointer to a union of type `AEArrayData`.
- [typealias AEArrayType](../coreservices/aearraytype.md)
  Stores a value that specifies an array type.
- [typealias AECoerceDescUPP](../coreservices/aecoercedescupp.md)
  Defines a data type for the universal procedure pointer for the `AECoerceDescProcPtr` callback function pointer.
- [typealias AECoercePtrUPP](../coreservices/aecoerceptrupp.md)
  Defines a data type for the universal procedure pointer for the `AECoercePtrProcPtr` callback function pointer.
- [typealias AECoercionHandlerUPP](../coreservices/aecoercionhandlerupp.md)
  Defines a data type for the universal procedure pointer for the `AECoercionHandlerUPP` callback function pointer.
- [typealias AEDataStorage](../coreservices/aedatastorage.md)
  A pointer to an opaque data type that provides storage for an `AEDesc` descriptor.
- [typealias AEDataStorageType](../coreservices/aedatastoragetype.md)
  An opaque data type used to store data in Apple event descriptors.
- [typealias AEDescList](../coreservices/aedesclist.md)
  A descriptor whose data consists of a list of one or more descriptors.
- [typealias AEEventSource](../coreservices/aeeventsource.md)
  A data type for values that specify how an Apple event was delivered.
- [typealias AEDisposeExternalUPP](../coreservices/aedisposeexternalupp.md)
  Defines a universal procedure pointer to a function the Apple Event Manager calls to dispose of a descriptor created by the `AECreateDescFromExternalPtr` function.
- [typealias AEEventClass](../coreservices/aeeventclass.md)
  Specifies the event class of an Apple event.
- [typealias AEEventHandlerUPP](../coreservices/aeeventhandlerupp.md)
  Defines a data type for the universal procedure pointer for the `AEEventHandlerUPP` callback function pointer.
- [typealias AEEventID](../coreservices/aeeventid.md)
  Specifies the event ID of an Apple event.
- [typealias AEKeyword](../coreservices/aekeyword.md)
  A four-character code that uniquely identifies a descriptor in an Apple event record or an Apple event.
- [typealias AERecord](../coreservices/aerecord.md)
  A descriptor whose data is a list of keyword-specified descriptors.
- [typealias AERemoteProcessResolverRef](../coreservices/aeremoteprocessresolverref.md)
  An opaque reference to an object that encapsulates the mechanism for obtaining a list of processes running on a remote machine.
- [typealias AEReturnID](../coreservices/aereturnid.md)
  Specifies a return ID for a created Apple event.
- [typealias AESendPriority](../coreservices/aesendpriority.md)
  Specifies the processing priority for a sent Apple event.
- [typealias AEStreamRef](../coreservices/aestreamref.md)
  An opaque data structure for storing stream-based descriptor data.
- [typealias AETransactionID](../coreservices/aetransactionid.md)
  Specifies a transaction ID.
- [typealias AppleEvent](../coreservices/appleevent.md)
  A descriptor whose data is a list of descriptors containing both attributes and parameters that make up an Apple event.
- [typealias DescType](../coreservices/desctype.md)
  Specifies the type of the data stored in an `AEDesc` descriptor.
- [typealias OffsetArrayHandle](../coreservices/offsetarrayhandle.md)
  Defines a data type that points to an `OffsetArray`. Not typically used by developers.
- [typealias OSLAccessorUPP](../coreservices/oslaccessorupp.md)
  Defines a data type for the universal procedure pointer for the `OSLAccessorProcPtr` callback function pointer.
- [typealias OSLAdjustMarksUPP](../coreservices/osladjustmarksupp.md)
  Defines a data type for the universal procedure pointer for the `OSLAdjustMarksProcPtr` callback function pointer.
- [typealias OSLCompareUPP](../coreservices/oslcompareupp.md)
  Defines a data type for the universal procedure pointer for the `OSLCompareProcPtr` callback function pointer.
- [typealias OSLCountUPP](../coreservices/oslcountupp.md)
  Defines a data type for the universal procedure pointer for the `OSLCountProcPtr` callback function pointer.
- [typealias OSLDisposeTokenUPP](../coreservices/osldisposetokenupp.md)
  Defines a data type for the universal procedure pointer for the `OSLDisposeTokenProcPtr` callback function pointer.
- [typealias OSLGetErrDescUPP](../coreservices/oslgeterrdescupp.md)
  Defines a data type for the universal procedure pointer for the `OSLGetErrDescProcPtr` callback function pointer.
- [typealias OSLGetMarkTokenUPP](../coreservices/oslgetmarktokenupp.md)
  Defines a data type for the universal procedure pointer for the `OSLGetMarkTokenProcPtr` callback function pointer.
- [typealias OSLMarkUPP](../coreservices/oslmarkupp.md)
  Defines a data type for the universal procedure pointer for the `OSLMarkProcPtr` callback function pointer.
### Constants
- [typealias AEBuildErrorCode](../coreservices/aebuilderrorcode.md)
  Represents syntax errors found by an Apple Event build routine.
- [typealias AESendMode](../coreservices/aesendmode.md)
  Specify send preferences to the `AESend` function.
- [Apple Event Recording Event ID Constants](../coreservices/apple_events/1527224-apple_event_recording_event_id_c.md)
  Specify event IDs for events that deal with Apple event recording.
- [cAEList](apple_event_manager/1556411-caelist.md)
- [Callback Constants for the AEResolve Function](../coreservices/apple_events/1572741-callback_constants_for_the_aeres.md)
  Specify supported callback features to the `AEResolve` function.
- [cInsertionLoc](apple_event_manager/1556389-cinsertionloc.md)
- [cKeystroke](apple_event_manager/1556385-ckeystroke.md)
- [Comparison Operator Constants](apple_event_manager/comparison_operator_constants.md)
  Specify a comparison operation to perform on two operands.
- [Constants for Object Specifiers, Positions, and Logical and Comparison Operations](../coreservices/apple_events/1572744-constants_for_object_specifiers_.md)
  Specify the types of the four keyword-specified descriptors that make up the data in an object specifier, as well as constants for position, logical operations, and comparison operations.
- [cURL](apple_event_manager/1556375-curl.md)
- [cVersion](apple_event_manager/cversion.md)
- [Data Array Constants](../coreservices/apple_events/1542848-data_array_constants.md)
  Specify an array type for storing or extracting descriptor lists with the `AEPutArray` and `AEGetArray` functions.
- [Descriptor Type Constants](../coreservices/apple_events/1542788-descriptor_type_constants.md)
  Specify types for descriptors.
- [eScheme](apple_event_manager/1556397-escheme.md)
- [Event Class Constants](../coreservices/apple_events/1527210-event_class_constants.md)
  Specify the event class for an Apple event.
- [Event ID Constants](../coreservices/apple_events/1527223-event_id_constants.md)
  Specify the event ID for an Apple event.
- [Event Source Constants](../coreservices/apple_events/1527201-event_source_constants.md)
  Identify how an Apple event was delivered.
- [Factoring Constants](../coreservices/apple_events/1542928-factoring_constants.md)
- [ID Constants for the AECreateAppleEvent Function](../coreservices/apple_events/1542799-id_constants_for_the_aecreateapp.md)
  Specify values for the ID parameters of the `AECreateAppleEvent` function.
- [Key Form and Descriptor Type Object Specifier Constants](../coreservices/apple_events/1572731-key_form_and_descriptor_type_obj.md)
  Specify possible values for the `keyAEKeyForm` field of an object specifier, as well as descriptor types used in resolving object specifiers.
- [Keyword Attribute Constants](../coreservices/apple_events/1542920-keyword_attribute_constants.md)
  Specify keyword values for Apple event attributes.
- [Keyword Parameter Constants](../coreservices/apple_events/1527206-keyword_parameter_constants.md)
  Specify keyword values for Apple event parameters, as well as information for the `AEManagerInfo` function to retrieve. Some common key word values are shown here.
- [Launch Apple Event Constants](../coreservices/apple_events/1556410-launch_apple_event_constants.md)
  In a `kAEOpenApplication` event, specify information about how the receiving application was launched.
- [Numeric Descriptor Type Constants](../coreservices/apple_events/1542872-numeric_descriptor_type_constant.md)
  Specify types for numeric descriptors.
- [Object Class ID Constants](../coreservices/apple_events/1556368-object_class_id_constants.md)
  Specify the object class for an Apple event object.
- [Other Descriptor Type Constants](../coreservices/apple_events/1542760-other_descriptor_type_constants.md)
  Specify types for Boolean and character descriptors.
- [Priority Constants for the AESend Function (Deprecated in macOS)](../coreservices/apple_events/1542840-priority_constants_for_the_aesen.md)
  Specify a value for the `sendPriority` parameter of the `AESend` function.
- [Remote Process Dictionary Keys](apple_event_manager/remote_process_dictionary_keys.md)
  Used to extract information from dictionaries with entries that describe remote processes.
- [Special Handler Callback Constants](../coreservices/apple_events/1572726-special_handler_callback_constan.md)
  Specify an object callback function to install, get, or remove from the special handler dispatch table.
- [Timeout Constants](../coreservices/apple_events/1542814-timeout_constants.md)
  Specify a timeout value.
- [Whose Test Constants](apple_event_manager/whose_test_constants.md)
- [kAEDoObjectsExist](apple_event_manager/kaedoobjectsexist.md)
- [kAEDebugPOSTHeader](../coreservices/apple_events/1542854-kaedebugpostheader.md)
- [kAEGetPrivilegeSelection](apple_event_manager/kaegetprivilegeselection.md)
- [kAEHandleArray](../coreservices/apple_events/1542886-kaehandlearray.md)
- [kAEInfo](../coreservices/apple_events/1556393-kaeinfo.md)
- [kAEInternetSuite](../coreservices/apple_events/1556388-kaeinternetsuite.md)
- [kAEISGetURL](../coreservices/apple_events/1556362-kaeisgeturl.md)
- [kAEISHTTPSearchArgs](../coreservices/apple_events/1556404-kaeishttpsearchargs.md)
- [kAELogOut](../coreservices/apple_events/1556395-kaelogout.md)
- [kAEMenuClass](../coreservices/apple_events/1556392-kaemenuclass.md)
- [kAEMouseClass](../coreservices/apple_events/1556409-kaemouseclass.md)
- [kAENonmodifiable](../coreservices/apple_events/1556386-kaenonmodifiable.md)
- [kAEQDNotOr](../coreservices/apple_events/1556377-kaeqdnotor.md)
- [kAESetPosition](../coreservices/apple_events/1556407-kaesetposition.md)
- [kAESocks4Protocol](../coreservices/apple_events/1542847-kaesocks4protocol.md)
- [kAEUseHTTPProxyAttr](../coreservices/apple_events/1542824-kaeusehttpproxyattr.md)
  Web Services Proxy support—these constants should be added as attributes of the event that is being sent (not as part of the direct object).
- [kAEUserTerminology](../coreservices/apple_events/1457902-kaeuserterminology.md)
- [kAEUseSocksAttr](../coreservices/apple_events/1542933-kaeusesocksattr.md)
- [kAEUTHasReturningParam](../coreservices/apple_events/1457911-kaeuthasreturningparam.md)
- [kAEZoomIn](../coreservices/apple_events/1556365-kaezoomin.md)
- [kBySmallIcon](apple_event_manager/1556391-kbysmallicon.md)
- [kConnSuite](apple_event_manager/1556369-kconnsuite.md)
- [keyAEAngle](../coreservices/apple_events/1556380-keyaeangle.md)
- [keyAEBaseAddr](../coreservices/apple_events/1556383-keyaebaseaddr.md)
- [keyAEDoScale](../coreservices/apple_events/1556387-keyaedoscale.md)
- [keyAEHiliteRange](../coreservices/apple_events/1556379-keyaehiliterange.md)
- [keyAEKeyword](../coreservices/apple_events/1556374-keyaekeyword.md)
- [keyAEPropData](apple_event_manager/keyaepropdata.md)
- [keyAESuiteID](../coreservices/apple_events/1556370-keyaesuiteid.md)
- [keyMenuID](../coreservices/apple_events/1556381-keymenuid.md)
- [keyMiscellaneous](../coreservices/apple_events/1556399-keymiscellaneous.md)
- [keyReplyPortAttr](../coreservices/apple_events/1571648-keyreplyportattr.md)
- [keySOAPStructureMetaData](../coreservices/apple_events/1542797-keysoapstructuremetadata.md)
- [keyUserNameAttr](../coreservices/apple_events/1542780-keyusernameattr.md)
- [kFAServerApp](apple_event_manager/1556384-kfaserverapp.md)
- [kLaunchToGetTerminology](apple_event_manager/1457909-klaunchtogetterminology.md)
- [kNextBody](apple_event_manager/1556402-knextbody.md)
- [kOSIZDontOpenResourceFile](apple_event_manager/1457903-kosizdontopenresourcefile.md)
- [kReadExtensionTermsMask](apple_event_manager/1457896-kreadextensiontermsmask.md)
- [kSOAP1999Schema](apple_event_manager/1542943-ksoap1999schema.md)
- [kTextServiceClass](apple_event_manager/1556406-ktextserviceclass.md)
- [kTSMHiliteCaretPosition](apple_event_manager/1556398-ktsmhilitecaretposition.md)
  Specify text highlighting information.
- [kTSMOutsideOfBody](apple_event_manager/1556371-ktsmoutsideofbody.md)
- [pArcAngle](apple_event_manager/1556376-parcangle.md)
- [pFormula](apple_event_manager/1556373-pformula.md)
- [pNewElementLoc](apple_event_manager/1556400-pnewelementloc.md)
- [pScheme](apple_event_manager/1556408-pscheme.md)
- [pTextStyles](apple_event_manager/1556367-ptextstyles.md)
- [typeAEText](apple_event_manager/1556366-typeaetext.md)
- [typeApplicationBundleID](apple_event_manager/1542896-typeapplicationbundleid.md)
  For specifying a target application by bundle ID.
- [typeFinderWindow](apple_event_manager/typefinderwindow.md)
- [typeHIMenu](apple_event_manager/1556372-typehimenu.md)
- [typeKernelProcessID](apple_event_manager/1542936-typekernelprocessid.md)
  For specifying an application by UNIX process ID.
- [typeMachPort](apple_event_manager/typemachport.md)
  For specifying a Mach port.
- [typeMeters](apple_event_manager/1556382-typemeters.md)
- [typePixelMap](apple_event_manager/typepixelmap.md)
- [typeReplyPortAttr](apple_event_manager/1571649-typereplyportattr.md)
- [typeTIFF](apple_event_manager/1556405-typetiff.md)
- [typeUnicodeText](apple_event_manager/1542918-typeunicodetext.md)
### Result Codes
- [var noPortErr: Int](../coreservices/noporterr.md)
  Client hasn’t set `'SIZE'` resource toindicate awareness of high-level events
- [var destPortErr: Int](../coreservices/destporterr.md)
  Server hasn’t set `'SIZE'` resource toindicate awareness of high-level events, or else is not present
- [var sessClosedErr: Int](../coreservices/sessclosederr.md)
  The `kAEDontReconnect` flagin the `sendMode` parameterwas set and the server quit, then restarted
- [var errAECoercionFail: Int](../coreservices/erraecoercionfail.md)
  Data could not be coerced to the requesteddescriptor type
- [var errAEDescNotFound: Int](../coreservices/erraedescnotfound.md)
  Descriptor was not found
- [var errAECorruptData: Int](../coreservices/erraecorruptdata.md)
  Data in an Apple event could not be read
- [var errAEWrongDataType: Int](../coreservices/erraewrongdatatype.md)
  Wrong descriptor type
- [var errAENotAEDesc: Int](../coreservices/erraenotaedesc.md)
  Not a valid descriptor
- [var errAEBadListItem: Int](../coreservices/erraebadlistitem.md)
  Operation involving a list item failed
- [var errAENewerVersion: Int](../coreservices/erraenewerversion.md)
  Need a newer version of the Apple EventManager
- [var errAENotAppleEvent: Int](../coreservices/erraenotappleevent.md)
  The event is not in AppleEvent format.
- [var errAEEventNotHandled: Int](../coreservices/erraeeventnothandled.md)
  Event wasn’t handled by an Apple eventhandler
- [var errAEReplyNotValid: Int](../coreservices/erraereplynotvalid.md)
  `AEResetTimer` was passed an invalid reply
- [var errAEUnknownSendMode: Int](../coreservices/erraeunknownsendmode.md)
  Invalid sending mode was passed
- [var errAEWaitCanceled: Int](../coreservices/erraewaitcanceled.md)
  User canceled out of wait loop for replyor receipt
- [var errAETimeout: Int](../coreservices/erraetimeout.md)
  Apple event timed out
- [var errAENoUserInteraction: Int](../coreservices/erraenouserinteraction.md)
  No user interaction allowed
- [var errAENotASpecialFunction: Int](../coreservices/erraenotaspecialfunction.md)
  Wrong keyword for a special function
- [var errAEParamMissed: Int](../coreservices/erraeparammissed.md)
  A required parameter was not accessed.
- [var errAEUnknownAddressType: Int](../coreservices/erraeunknownaddresstype.md)
  Unknown Apple event address type
- [var errAEHandlerNotFound: Int](../coreservices/erraehandlernotfound.md)
  No handler found for an Apple event
- [var errAEReplyNotArrived: Int](../coreservices/erraereplynotarrived.md)
  Reply has not yet arrived
- [var errAEIllegalIndex: Int](../coreservices/erraeillegalindex.md)
  Not a valid list index
- [var errAEImpossibleRange: Int](../coreservices/erraeimpossiblerange.md)
  The range is not valid because it is impossiblefor a range to include the first and last objects that were specified;an example is a range in which the offset of the first object is greaterthan the offset of the last object
- [var errAEWrongNumberArgs: Int](../coreservices/erraewrongnumberargs.md)
  The number of operands provided for the `kAENOT` logicaloperator is not 1
- [var errAEAccessorNotFound: Int](../coreservices/erraeaccessornotfound.md)
  There is no object accessor function forthe specified object class and container type
- [var errAENoSuchLogical: Int](../coreservices/erraenosuchlogical.md)
  The logical operator in a logical descriptoris not `kAEAND`, `kAEOR`,or `kAENOT`
- [var errAEBadTestKey: Int](../coreservices/erraebadtestkey.md)
  The descriptor in a test key is neithera comparison descriptor nor a logical descriptor
- [var errAENoSuchObject: Int](../coreservices/erraenosuchobject.md)
  Runtime resolution of an object failed.
- [var errAENegativeCount: Int](../coreservices/erraenegativecount.md)
  An object-counting function returned a negativeresult
- [var errAEEmptyListContainer: Int](../coreservices/erraeemptylistcontainer.md)
  The container for an Apple event objectis specified by an empty list
- [var errAEUnknownObjectType: Int](../coreservices/erraeunknownobjecttype.md)
  The object type isn’t recognized
- [var errAERecordingIsAlreadyOn: Int](../coreservices/erraerecordingisalreadyon.md)
  Recording is already on
- [var errAEReceiveTerminate: Int](../coreservices/erraereceiveterminate.md)
  Break out of all levels of `AEReceive` tothe topmost (1.1 or greater)
- [var errAEReceiveEscapeCurrent: Int](../coreservices/erraereceiveescapecurrent.md)
  Break out of lowest level only of `AEReceive` (1.1or greater)
- [var errAEEventFiltered: Int](../coreservices/erraeeventfiltered.md)
  Event has been filtered and should not bepropagated (1.1 or greater)
- [var errAEDuplicateHandler: Int](../coreservices/erraeduplicatehandler.md)
  Attempt to install handler in table foridentical class and ID (1.1 or greater)
- [var errAEStreamBadNesting: Int](../coreservices/erraestreambadnesting.md)
  Nesting violation while streaming
- [var errAEStreamAlreadyConverted: Int](../coreservices/erraestreamalreadyconverted.md)
  Attempt to convert a stream that has alreadybeen converted
- [var errAEDescIsNull: Int](../coreservices/erraedescisnull.md)
  Attempt to perform an invalid operationon a null descriptor
- [var errAEBuildSyntaxError: Int](../coreservices/erraebuildsyntaxerror.md)
  `AEBuildDesc` andrelated functions detected a syntax error
- [var errAEBufferTooSmall: Int](../coreservices/erraebuffertoosmall.md)
  Buffer for `AEFlattenDesc` toosmall
- [var errASCantConsiderAndIgnore: Int](../coreservices/errascantconsiderandignore.md)
  Can’t both consider and ignore <attribute>.
- [var errASCantCompareMoreThan32k: Int](../coreservices/errascantcomparemorethan32k.md)
  Can’t perform operation on text longerthan 32K bytes.
- [var errASTerminologyNestingTooDeep: Int](../coreservices/errasterminologynestingtoodeep.md)
  Tell statements are nested too deeply.
- [var errASIllegalFormalParameter: Int](../coreservices/errasillegalformalparameter.md)
  <name> is illegal as a formal parameter.
- [var errASParameterNotForEvent: Int](../coreservices/errasparameternotforevent.md)
  <name> is not a parameter name for the event <event>.
- [var errASNoResultReturned: Int](../coreservices/errasnoresultreturned.md)
  No result was returned for some argumentof this expression. 
- [var errAEEventFailed: Int](../coreservices/erraeeventfailed.md)
  Apple event handler failed.
- [var errAETypeError: Int](../coreservices/erraetypeerror.md)
  A descriptor type mismatch occurred.
- [var errAEBadKeyForm: Int](../coreservices/erraebadkeyform.md)
  Invalid key form.
- [var errAENotModifiable: Int](../coreservices/erraenotmodifiable.md)
  Can't set <object or data> to <object or data>. Access not allowed.
- [var errAEPrivilegeError: Int](../coreservices/erraeprivilegeerror.md)
  A privilege violation occurred.
- [var errAEReadDenied: Int](../coreservices/erraereaddenied.md)
  The read operation was not allowed.
- [var errAEWriteDenied: Int](../coreservices/erraewritedenied.md)
  Can't set <object or data> to <object or data>. 
- [var errAEIndexTooLarge: Int](../coreservices/erraeindextoolarge.md)
  The index of the event is too large to bevalid.
- [var errAENotAnElement: Int](../coreservices/erraenotanelement.md)
  The specified object is a property, notan element.
- [var errAECantSupplyType: Int](../coreservices/erraecantsupplytype.md)
  Can’t supply the requested descriptortype for the data.
- [var errAECantHandleClass: Int](../coreservices/erraecanthandleclass.md)
  The Apple event handler can’t handle objectsof this class.
- [var errAEInTransaction: Int](../coreservices/erraeintransaction.md)
  Couldn’t handle this command because itwasn’t part of the current transaction.
- [var errAENoSuchTransaction: Int](../coreservices/erraenosuchtransaction.md)
  The transaction to which this command belongedisn’t a valid transaction.
- [var errAENoUserSelection: Int](../coreservices/erraenouserselection.md)
  There is no user selection.
- [var errAENotASingleObject: Int](../coreservices/erraenotasingleobject.md)
  Handler only handles single objects.
- [var errAECantUndo: Int](../coreservices/erraecantundo.md)
  Can’t undo the previous Apple event oruser action.
- [var errAENotAnEnumMember: Int](../coreservices/erraenotanenummember.md)
  Enumerated value in `SetData` is notallowed for this property
- [var errAECantPutThatThere: Int](../coreservices/erraecantputthatthere.md)
  In make new, duplicate, etc. class can'tbe an element of container
- [var errAEPropertiesClash: Int](../coreservices/erraepropertiesclash.md)
  Illegal combination of properties settingsfor SetData, make new, or duplicate

## See Also

- [ColorSync Manager](colorsync_manager.md)
- [Speech Synthesis Manager](speech_synthesis_manager.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager)*