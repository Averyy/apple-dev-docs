# Apple Events

**Framework**: Core Services

Communicate messages across process boundaries that can be performed and responded to with a reply event.

#### Overview

When a script that targets an application is executed, commands are sent to the application in the form of , a kind of interprocess message. Cocoa scripting helps you create scriptable applications by doing much of the work of receiving these Apple events, extracting information from them, and invoking methods in your scriptable classes.

## Topics

### Structures
- [func AECallObjectAccessor(DescType, UnsafePointer<AEDesc>!, DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](1447059-aecallobjectaccessor.md)
  Invokes the appropriate object accessor function for a specific desired type and container type. 
- [func AECheckIsRecord(UnsafePointer<AEDesc>!) -> Bool](1444011-aecheckisrecord.md)
  Determines whether a descriptor is truly an `AERecord`.
- [func AECoerceDesc(UnsafePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](1446519-aecoercedesc.md)
  Coerces the data in a descriptor to another descriptor type and creates a descriptor containing the newly coerced data.
- [func AECoercePtr(DescType, UnsafeRawPointer!, Size, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](1441846-aecoerceptr.md)
  Coerces data to a desired descriptor type and creates a descriptor containing the newly coerced data.
- [func AECompareDesc(UnsafePointer<AEDesc>!, UnsafePointer<AEDesc>!, UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus](1448782-aecomparedesc.md)
- [func AECountItems(UnsafePointer<AEDescList>!, UnsafeMutablePointer<Int>!) -> OSErr](1449533-aecountitems.md)
  Counts the number of descriptors in a descriptor list.
- [func AECreateAppleEvent(AEEventClass, AEEventID, UnsafePointer<AEAddressDesc>!, AEReturnID, AETransactionID, UnsafeMutablePointer<AppleEvent>!) -> OSErr](1448525-aecreateappleevent.md)
  Creates an Apple event with several important attributes but no parameters.
- [func AECreateDesc(DescType, UnsafeRawPointer!, Size, UnsafeMutablePointer<AEDesc>!) -> OSErr](1448535-aecreatedesc.md)
  Creates a new descriptor that incorporates the specified data.
- [func AECreateDescFromExternalPtr(OSType, UnsafeRawPointer!, Size, AEDisposeExternalUPP!, SRefCon!, UnsafeMutablePointer<AEDesc>!) -> OSStatus](1446239-aecreatedescfromexternalptr.md)
  Creates a new descriptor that uses a memory buffer supplied by the caller.
- [func AECreateList(UnsafeRawPointer!, Size, Bool, UnsafeMutablePointer<AEDescList>!) -> OSErr](1448643-aecreatelist.md)
  Creates an empty descriptor list or Apple event record.
- [func AECreateRemoteProcessResolver(CFAllocator!, CFURL!) -> AERemoteProcessResolverRef!](1445692-aecreateremoteprocessresolver.md)
  Creates an object for resolving a list of remote processes.
- [func AEDecodeMessage(UnsafeMutablePointer<mach_msg_header_t>!, UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AppleEvent>!) -> OSStatus](1447827-aedecodemessage.md)
  Decodes a Mach message and converts it into an Apple event and its related reply.
- [func AEDeleteItem(UnsafeMutablePointer<AEDescList>!, Int) -> OSErr](1447164-aedeleteitem.md)
  Deletes a descriptor from a descriptor list, causing all subsequent descriptors to move up one place. 
- [func AEDeleteParam(UnsafeMutablePointer<AppleEvent>!, AEKeyword) -> OSErr](1444338-aedeleteparam.md)
  Deletes a keyword-specified parameter from an Apple event record.
- [func AEDisposeDesc(UnsafeMutablePointer<AEDesc>!) -> OSErr](1444208-aedisposedesc.md)
  Deallocates the memory used by a descriptor.
- [func AEDisposeRemoteProcessResolver(AERemoteProcessResolverRef!)](1442572-aedisposeremoteprocessresolver.md)
  Disposes of an `AERemoteProcessResolverRef`.
- [func AEDisposeToken(UnsafeMutablePointer<AEDesc>!) -> OSErr](1446783-aedisposetoken.md)
  Deallocates the memory used by a token.
- [func AEDuplicateDesc(UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](1442661-aeduplicatedesc.md)
  Creates a copy of a descriptor.
- [func AEFlattenDesc(UnsafePointer<AEDesc>!, Ptr!, Size, UnsafeMutablePointer<Size>!) -> OSStatus](1441808-aeflattendesc.md)
  Flattens the specified descriptor and stores the data in the supplied buffer.
- [func AEGetArray(UnsafePointer<AEDescList>!, AEArrayType, AEArrayDataPointer!, Size, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!, UnsafeMutablePointer<Int>!) -> OSErr](1445720-aegetarray.md)
  Extracts data from an Apple event array created with the `AEPutArray` function and stores it as a standard array of fixed size items in the specified buffer.
- [func AEGetAttributeDesc(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](1450314-aegetattributedesc.md)
  Gets a copy of the descriptor for a specified Apple event attribute from an Apple event; typically used when your application needs to pass the descriptor on to another function.
- [func AEGetAttributePtr(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](1445109-aegetattributeptr.md)
  Gets a copy of the data for a specified Apple event attribute from an Apple event; typically used when your application needs to work with the data directly.
- [func AEGetCoercionHandler(DescType, DescType, UnsafeMutablePointer<AECoercionHandlerUPP?>!, UnsafeMutablePointer<SRefCon?>!, UnsafeMutablePointer<DarwinBoolean>!, Bool) -> OSErr](1445348-aegetcoercionhandler.md)
  Gets the coercion handler for a specified descriptor type.
- [func AEGetDescData(UnsafePointer<AEDesc>!, UnsafeMutableRawPointer!, Size) -> OSErr](1444427-aegetdescdata.md)
  Gets the data from the specified descriptor.
- [func AEGetDescDataRange(UnsafePointer<AEDesc>!, UnsafeMutableRawPointer!, Size, Size) -> OSStatus](1446560-aegetdescdatarange.md)
  Retrieves a specified series of bytes from the specified descriptor.
- [func AEGetDescDataSize(UnsafePointer<AEDesc>!) -> Size](1450119-aegetdescdatasize.md)
  Gets the size, in bytes, of the data in the specified descriptor.
- [func AEGetEventHandler(AEEventClass, AEEventID, UnsafeMutablePointer<AEEventHandlerUPP?>!, UnsafeMutablePointer<SRefCon?>!, Bool) -> OSErr](1445631-aegeteventhandler.md)
  Gets an event handler from an Apple event dispatch table.
- [func AEGetNthDesc(UnsafePointer<AEDescList>!, Int, DescType, UnsafeMutablePointer<AEKeyword>!, UnsafeMutablePointer<AEDesc>!) -> OSErr](1448326-aegetnthdesc.md)
   Copies a descriptor from a specified position in a descriptor list into a specified descriptor; typically used when your application needs to pass the extracted data to another function as a descriptor.
- [func AEGetNthPtr(UnsafePointer<AEDescList>!, Int, DescType, UnsafeMutablePointer<AEKeyword>!, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](1447539-aegetnthptr.md)
  Gets a copy of the data from a descriptor at a specified position in a descriptor list; typically used when your application needs to work with the extracted data directly.
- [func AEGetObjectAccessor(DescType, DescType, UnsafeMutablePointer<OSLAccessorUPP?>!, UnsafeMutablePointer<SRefCon?>!, Bool) -> OSErr](1449054-aegetobjectaccessor.md)
  Gets an object accessor function from an object accessor dispatch table. 
- [func AEGetParamDesc(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<AEDesc>!) -> OSErr](1449233-aegetparamdesc.md)
  Gets a copy of the descriptor for a keyword-specified Apple event parameter from an Apple event or an Apple event record.
- [func AEGetParamPtr(UnsafePointer<AppleEvent>!, AEKeyword, DescType, UnsafeMutablePointer<DescType>!, UnsafeMutableRawPointer!, Size, UnsafeMutablePointer<Size>!) -> OSErr](1444069-aegetparamptr.md)
  Gets a copy of the data for a specified Apple event parameter from an Apple event or an Apple event record.
- [func AEGetRegisteredMachPort() -> mach_port_t](1449736-aegetregisteredmachport.md)
  Returns the Mach port (in the form of a `mach_port_t`) that was registered with the bootstrap server for this process.
- [func AEGetSpecialHandler(AEKeyword, UnsafeMutablePointer<AEEventHandlerUPP?>!, Bool) -> OSErr](1444274-aegetspecialhandler.md)
  Gets a specified handler from a special handler dispatch table.
- [func AEInitializeDesc(UnsafeMutablePointer<AEDesc>!)](1446047-aeinitializedesc.md)
  Initializes a new descriptor. 
- [func AEInstallCoercionHandler(DescType, DescType, AECoercionHandlerUPP!, SRefCon!, Bool, Bool) -> OSErr](1445548-aeinstallcoercionhandler.md)
  Installs a coercion handler in either the application or system coercion handler dispatch table.
- [func AEInstallEventHandler(AEEventClass, AEEventID, AEEventHandlerUPP!, SRefCon!, Bool) -> OSErr](1448596-aeinstalleventhandler.md)
  Adds an entry for an event handler to an Apple event dispatch table.
- [func AEInstallObjectAccessor(DescType, DescType, OSLAccessorUPP!, SRefCon!, Bool) -> OSErr](1447905-aeinstallobjectaccessor.md)
  Adds or replaces an entry for an object accessor function to an object accessor dispatch table.
- [func AEInstallSpecialHandler(AEKeyword, AEEventHandlerUPP!, Bool) -> OSErr](1445532-aeinstallspecialhandler.md)
  Installs a callback function in a special handler dispatch table.
- [func AEManagerInfo(AEKeyword, UnsafeMutablePointer<Int>!) -> OSErr](1449373-aemanagerinfo.md)
  Provides information about the version of the Apple Event Manager currently available or the number of processes that are currently recording Apple events.
- [func AEObjectInit() -> OSErr](1447372-aeobjectinit.md)
  Initializes the Object Support Library.
- [func AEPrintDescToHandle(UnsafePointer<AEDesc>!, UnsafeMutablePointer<Handle?>!) -> OSStatus](1445158-aeprintdesctohandle.md)
  Provides a pretty printer facility for displaying the contents of Apple event descriptors.
- [func AEProcessMessage(UnsafeMutablePointer<mach_msg_header_t>!) -> OSStatus](1444387-aeprocessmessage.md)
  Decodes and dispatches a low level Mach message event to an event handler, including packaging and returning the reply to the sender.
- [func AEPutArray(UnsafeMutablePointer<AEDescList>!, AEArrayType, UnsafePointer<AEArrayData>!, DescType, Size, Int) -> OSErr](1442535-aeputarray.md)
  Inserts the data for an Apple event array into a descriptor list, replacing any previous descriptors in the list.
- [func AEPutAttributeDesc(UnsafeMutablePointer<AppleEvent>!, AEKeyword, UnsafePointer<AEDesc>!) -> OSErr](1441790-aeputattributedesc.md)
  Adds a descriptor and a keyword to an Apple event as an attribute.
- [func AEPutAttributePtr(UnsafeMutablePointer<AppleEvent>!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSErr](1445940-aeputattributeptr.md)
  Adds a pointer to data, a descriptor type, and a keyword to an Apple event as an attribute.
- [func AEPutDesc(UnsafeMutablePointer<AEDescList>!, Int, UnsafePointer<AEDesc>!) -> OSErr](1450093-aeputdesc.md)
  Adds a descriptor to any descriptor list, possibly replacing an existing descriptor in the list.
- [func AEPutParamDesc(UnsafeMutablePointer<AppleEvent>!, AEKeyword, UnsafePointer<AEDesc>!) -> OSErr](1447576-aeputparamdesc.md)
  Inserts a descriptor and a keyword into an Apple event or Apple event record as an Apple event parameter.
- [func AEPutParamPtr(UnsafeMutablePointer<AppleEvent>!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSErr](1449263-aeputparamptr.md)
  Inserts data, a descriptor type, and a keyword into an Apple event or Apple event record as an Apple event parameter.
- [func AEPutPtr(UnsafeMutablePointer<AEDescList>!, Int, DescType, UnsafeRawPointer!, Size) -> OSErr](1445287-aeputptr.md)
  Inserts data specified in a buffer into a descriptor list as a descriptor, possibly replacing an existing descriptor in the list.
- [func AERemoteProcessResolverGetProcesses(AERemoteProcessResolverRef!, UnsafeMutablePointer<CFStreamError>!) -> Unmanaged<CFArray>!](1444456-aeremoteprocessresolvergetproces.md)
  Returns an array of objects containing information about processes running on a remote machine.
- [func AERemoteProcessResolverScheduleWithRunLoop(AERemoteProcessResolverRef!, CFRunLoop!, CFString!, AERemoteProcessResolverCallback!, UnsafePointer<AERemoteProcessResolverContext>!)](1447259-aeremoteprocessresolverschedulew.md)
  Schedules a resolver for execution on a given run loop in a given mode.
- [func AERemoveCoercionHandler(DescType, DescType, AECoercionHandlerUPP!, Bool) -> OSErr](1441907-aeremovecoercionhandler.md)
  Removes a coercion handler from a coercion handler dispatch table.
- [func AERemoveEventHandler(AEEventClass, AEEventID, AEEventHandlerUPP!, Bool) -> OSErr](1445239-aeremoveeventhandler.md)
  Removes an event handler entry from an Apple event dispatch table.
- [func AERemoveObjectAccessor(DescType, DescType, OSLAccessorUPP!, Bool) -> OSErr](1442552-aeremoveobjectaccessor.md)
  Removes an object accessor function from an object accessor dispatch table. 
- [func AERemoveSpecialHandler(AEKeyword, AEEventHandlerUPP!, Bool) -> OSErr](1447960-aeremovespecialhandler.md)
  Removes a handler from a special handler dispatch table.
- [func AEReplaceDescData(DescType, UnsafeRawPointer!, Size, UnsafeMutablePointer<AEDesc>!) -> OSErr](1446695-aereplacedescdata.md)
  Copies the specified data into the specified descriptor, replacing any previous data.
- [func AEResolve(UnsafePointer<AEDesc>!, Int16, UnsafeMutablePointer<AEDesc>!) -> OSErr](1449720-aeresolve.md)
  Resolves an object specifier.
- [func AESendMessage(UnsafePointer<AppleEvent>!, UnsafeMutablePointer<AppleEvent>!, AESendMode, Int) -> OSStatus](1442994-aesendmessage.md)
  Sends an AppleEvent to a target process without some of the overhead required by `AESend`.
- [func AESetObjectCallbacks(OSLCompareUPP!, OSLCountUPP!, OSLDisposeTokenUPP!, OSLGetMarkTokenUPP!, OSLMarkUPP!, OSLAdjustMarksUPP!, OSLGetErrDescUPP!) -> OSErr](1447756-aesetobjectcallbacks.md)
  Specifies the object callback functions for your application.
- [func AESizeOfAttribute(UnsafePointer<AppleEvent>!, AEKeyword, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](1445764-aesizeofattribute.md)
  Gets the size and descriptor type of an Apple event attribute from a descriptor of type `AppleEvent`.
- [func AESizeOfFlattenedDesc(UnsafePointer<AEDesc>!) -> Size](1447305-aesizeofflatteneddesc.md)
  Returns the amount of buffer space needed to store the descriptor after flattening it.
- [func AESizeOfNthItem(UnsafePointer<AEDescList>!, Int, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](1447307-aesizeofnthitem.md)
  Gets the data size and descriptor type of the descriptor at a specified position in a descriptor list.
- [func AESizeOfParam(UnsafePointer<AppleEvent>!, AEKeyword, UnsafeMutablePointer<DescType>!, UnsafeMutablePointer<Size>!) -> OSErr](1449998-aesizeofparam.md)
  Gets the size and descriptor type of an Apple event parameter from a descriptor of type `AERecord` or `AppleEvent`.
- [func AEStreamClose(AEStreamRef!, UnsafeMutablePointer<AEDesc>!) -> OSStatus](1449821-aestreamclose.md)
  Closes and deallocates an `AEStreamRef`.
- [func AEStreamCloseDesc(AEStreamRef!) -> OSStatus](1449272-aestreamclosedesc.md)
  Marks the end of a descriptor in an `AEStreamRef`.
- [func AEStreamCloseList(AEStreamRef!) -> OSStatus](1448185-aestreamcloselist.md)
  Marks the end of a list of descriptors in an `AEStreamRef`.
- [func AEStreamCloseRecord(AEStreamRef!) -> OSStatus](1449522-aestreamcloserecord.md)
  Marks the end of a record in an `AEStreamRef`.
- [func AEStreamCreateEvent(AEEventClass, AEEventID, DescType, UnsafeRawPointer!, Size, Int16, Int32) -> AEStreamRef!](1446562-aestreamcreateevent.md)
  Creates a new Apple event and opens a stream for writing data to it.
- [func AEStreamOpen() -> AEStreamRef!](1447732-aestreamopen.md)
  Opens a new `AEStreamRef` for use in building a descriptor.
- [func AEStreamOpenDesc(AEStreamRef!, DescType) -> OSStatus](1446544-aestreamopendesc.md)
  Marks the beginning of a descriptor in an `AEStreamRef`.
- [func AEStreamOpenEvent(UnsafeMutablePointer<AppleEvent>!) -> AEStreamRef!](1445366-aestreamopenevent.md)
  Opens a stream for an existing Apple event.
- [func AEStreamOpenKeyDesc(AEStreamRef!, AEKeyword, DescType) -> OSStatus](1442897-aestreamopenkeydesc.md)
  Marks the beginning of a key descriptor in an `AEStreamRef`.
- [func AEStreamOpenList(AEStreamRef!) -> OSStatus](1448594-aestreamopenlist.md)
  Marks the beginning of a descriptor list in an `AEStreamRef`.
- [func AEStreamOpenRecord(AEStreamRef!, DescType) -> OSStatus](1447141-aestreamopenrecord.md)
  Marks the beginning of an Apple event record in an `AEStreamRef`.
- [func AEStreamOptionalParam(AEStreamRef!, AEKeyword) -> OSStatus](1444481-aestreamoptionalparam.md)
  Designates a parameter in an Apple event as optional.
- [func AEStreamSetRecordType(AEStreamRef!, DescType) -> OSStatus](1447704-aestreamsetrecordtype.md)
  Sets the type of the most recently created record in an `AEStreamRef`.
- [func AEStreamWriteAEDesc(AEStreamRef!, UnsafePointer<AEDesc>!) -> OSStatus](1448487-aestreamwriteaedesc.md)
  Copies an existing descriptor into an `AEStreamRef`.
- [func AEStreamWriteData(AEStreamRef!, UnsafeRawPointer!, Size) -> OSStatus](1442610-aestreamwritedata.md)
  Appends data to the current descriptor in an `AEStreamRef`.
- [func AEStreamWriteDesc(AEStreamRef!, DescType, UnsafeRawPointer!, Size) -> OSStatus](1450387-aestreamwritedesc.md)
  Appends the data for a complete descriptor to an `AEStreamRef`.
- [func AEStreamWriteKey(AEStreamRef!, AEKeyword) -> OSStatus](1448750-aestreamwritekey.md)
  Marks the beginning of a keyword/descriptor pair for a descriptor in an `AEStreamRef`.
- [func AEStreamWriteKeyDesc(AEStreamRef!, AEKeyword, DescType, UnsafeRawPointer!, Size) -> OSStatus](1442568-aestreamwritekeydesc.md)
  Writes a complete keyword/descriptor pair to an `AEStreamRef`.
- [func AEUnflattenDesc(UnsafeRawPointer!, UnsafeMutablePointer<AEDesc>!) -> OSStatus](1448997-aeunflattendesc.md)
  Unflattens the data in the passed buffer and creates a descriptor from it.
- [struct AEArrayData](aearraydata.md)
  Stores array information to be put into a descriptor listwith the `AEPutArray` functionor extracted from a descriptor list with the `AEGetArray` function.
- [struct AEBuildError](aebuilderror.md)
  Defines a structure for storing additional error codeinformation for “AEBuild” routines.
- [struct AEDesc](aedesc.md)
  Stores data and an accompanying descriptor type to formthe basic building block of all Apple Events.
- [struct AEKeyDesc](aekeydesc.md)
  Associates a keyword with a descriptor to form a keyword-specifieddescriptor.
- [struct AERemoteProcessResolverContext](aeremoteprocessresolvercontext.md)
  Supplied as a parameter when performing asynchronous resolutionof remote processes.
### Constants
- [let kAERemoteProcessNameKey: CFString!](kaeremoteprocessnamekey.md)
  Use this key to obtain the visible name of the remote process, in the localization supplied by the server, as a `CFStringRef`.
- [let kAERemoteProcessProcessIDKey: CFString!](kaeremoteprocessprocessidkey.md)
  Use this key to obtain the process ID of the remote process, if available; if so, returned as a `CFNumberRef`.
- [let kAERemoteProcessURLKey: CFString!](kaeremoteprocessurlkey.md)
  Use this key to obtain the full URL to the remote process, as a `CFURLRef`.
- [let kAERemoteProcessUserIDKey: CFString!](kaeremoteprocessuseridkey.md)
  Use this key to obtain the user ID of the remote process, if available; if so, returned as a `CFNumberRef`.
### Data Types
- [typealias OSLAccessorProcPtr](oslaccessorprocptr.md)
  Your object accessor function either finds elements or properties of an Apple event object.
- [typealias OSLAccessorUPP](oslaccessorupp.md)
  Defines a data type for the universal procedure pointer for the `OSLAccessorProcPtr` callback function pointer.
- [typealias OSLAdjustMarksProcPtr](osladjustmarksprocptr.md)
  Defines a pointer to an adjust marks callback function. Your adjust marks function unmarks objects previously marked by a call to your marking function.
- [typealias OSLAdjustMarksUPP](osladjustmarksupp.md)
  Defines a data type for the universal procedure pointer for the `OSLAdjustMarksProcPtr` callback function pointer.
- [typealias OSLCompareProcPtr](oslcompareprocptr.md)
  Defines a pointer to an object comparison callback function. Your object comparison function compares one Apple event object to another or to the data for a descriptor.
- [typealias OSLCompareUPP](oslcompareupp.md)
  Defines a data type for the universal procedure pointer for the `OSLCompareProcPtr` callback function pointer.
- [typealias OSLCountProcPtr](oslcountprocptr.md)
  Defines a pointer to an object counting callback function. Your object counting function counts the number of Apple event objects of a specified class in a specified container object.
- [typealias OSLCountUPP](oslcountupp.md)
  Defines a data type for the universal procedure pointer for the `OSLCountProcPtr` callback function pointer.
- [typealias OSLDisposeTokenProcPtr](osldisposetokenprocptr.md)
  Defines a pointer to a dispose token callback function. Your dispose token function, required only if you use a complex token format, disposes of the specified token.
- [typealias OSLDisposeTokenUPP](osldisposetokenupp.md)
  Defines a data type for the universal procedure pointer for the `OSLDisposeTokenProcPtr` callback function pointer.
- [typealias OSLGetErrDescProcPtr](oslgeterrdescprocptr.md)
  Defines a pointer to an error descriptor callback function. Your error descriptor callback function supplies a pointer to an address where the Apple Event Manager can store the current descriptor if an error occurs during a call to the `AEResolve` function.
- [typealias OSLGetErrDescUPP](oslgeterrdescupp.md)
  Defines a data type for the universal procedure pointer for the `OSLGetErrDescProcPtr` callback function pointer.
- [typealias OSLGetMarkTokenProcPtr](oslgetmarktokenprocptr.md)
  Defines a pointer to a mark token callback function. Your mark token function returns a mark token.
- [typealias OSLGetMarkTokenUPP](oslgetmarktokenupp.md)
  Defines a data type for the universal procedure pointer for the `OSLGetMarkTokenProcPtr` callback function pointer.
- [typealias OSLMarkProcPtr](oslmarkprocptr.md)
  Defines a pointer to an object marking callback function. Your object-marking function marks a specific Apple event object.
- [typealias OSLMarkUPP](oslmarkupp.md)
  Defines a data type for the universal procedure pointer for the `OSLMarkProcPtr` callback function pointer.
- [typealias AEAddressDesc](aeaddressdesc.md)
  A descriptor that contains the address of an application, used to describe the target application for an Apple event.
- [typealias AEArrayDataPointer](aearraydatapointer.md)
  A pointer to a union of type `AEArrayData`.
- [typealias AEArrayType](aearraytype.md)
  Stores a value that specifies an array type.
- [typealias AEBuildErrorCode](aebuilderrorcode.md)
  Represents syntax errors found by an Apple Event build routine.
- [typealias AECoerceDescProcPtr](aecoercedescprocptr.md)
  Defines a pointer to a function that coerces data stored in a descriptor. Your descriptor coercion callback function coerces the data from the passed descriptor to the specified type, returning the coerced data in a second descriptor.
- [typealias AECoerceDescUPP](aecoercedescupp.md)
  Defines a data type for the universal procedure pointer for the `AECoerceDescProcPtr` callback function pointer.
- [typealias AECoercePtrProcPtr](aecoerceptrprocptr.md)
  Defines a pointer to a function that coerces data stored in a buffer. Your pointer coercion callback routine coerces the data from the passed buffer to the specified type, returning the coerced data in a descriptor.
- [typealias AECoercePtrUPP](aecoerceptrupp.md)
  Defines a data type for the universal procedure pointer for the `AECoercePtrProcPtr` callback function pointer.
- [typealias AECoercionHandlerUPP](aecoercionhandlerupp.md)
  Defines a data type for the universal procedure pointer for the `AECoercionHandlerUPP` callback function pointer.
- [typealias AEDataStorage](aedatastorage.md)
  A pointer to an opaque data type that provides storage for an `AEDesc` descriptor.
- [typealias AEDataStorageType](aedatastoragetype.md)
  An opaque data type used to store data in Apple event descriptors.
- [typealias AEDescList](aedesclist.md)
  A descriptor whose data consists of a list of one or more descriptors.
- [typealias AEDescPtr](aedescptr.md)
- [typealias AEDisposeExternalProcPtr](aedisposeexternalprocptr.md)
  Defines a pointer to a function the Apple Event Manager calls to dispose of a descriptor created by the `AECreateDescFromExternalPtr` function. Your callback function disposes of the buffer you originally passed to that function.
- [typealias AEDisposeExternalUPP](aedisposeexternalupp.md)
  Defines a universal procedure pointer to a function the Apple Event Manager calls to dispose of a descriptor created by the `AECreateDescFromExternalPtr` function.
- [typealias AEEventClass](aeeventclass.md)
  Specifies the event class of an Apple event.
- [typealias AEEventHandlerProcPtr](aeeventhandlerprocptr.md)
  Defines a pointer to a function that handles one or more Apple events. Your Apple event handler function performs any action requested by the Apple event, adds parameters to the reply Apple event if appropriate (possibly including error information), and returns a result code.
- [typealias AEEventHandlerUPP](aeeventhandlerupp.md)
  Defines a data type for the universal procedure pointer for the `AEEventHandlerUPP` callback function pointer.
- [typealias AEEventID](aeeventid.md)
  Specifies the event ID of an Apple event.
- [typealias AEEventSource](aeeventsource.md)
  A data type for values that specify how an Apple event was delivered.
- [typealias AEKeyword](aekeyword.md)
  A four-character code that uniquely identifies a descriptor in an Apple event record or an Apple event.
- [typealias AERecord](aerecord.md)
  A descriptor whose data is a list of keyword-specified descriptors.
- [typealias AERemoteProcessResolverCallback](aeremoteprocessresolvercallback.md)
  Defines a pointer to a function the Apple Event Manager calls when the asynchronous execution of a remote process resolver completes, either due to success or failure, after a call to the `AERemoteProcessResolverScheduleWithRunLoop` function. Your callback function can use the reference passed to it to get the remote process information.
- [typealias AERemoteProcessResolverRef](aeremoteprocessresolverref.md)
  An opaque reference to an object that encapsulates the mechanism for obtaining a list of processes running on a remote machine.
- [typealias AEReturnID](aereturnid.md)
  Specifies a return ID for a created Apple event.
- [typealias AESendMode](aesendmode.md)
  Specify send preferences to the `AESend` function.
- [typealias AESendPriority](aesendpriority.md)
  Specifies the processing priority for a sent Apple event.
- [typealias AEStreamRef](aestreamref.md)
  An opaque data structure for storing stream-based descriptor data.
- [typealias AETransactionID](aetransactionid.md)
  Specifies a transaction ID.
### Enumerations
- [kAEDebugPOSTHeader](apple_events/1542854-kaedebugpostheader.md)
- [kAEHandleArray](apple_events/1542886-kaehandlearray.md)
- [kAEISGetURL](apple_events/1556362-kaeisgeturl.md)
- [kAEISHTTPSearchArgs](apple_events/1556404-kaeishttpsearchargs.md)
- [kAEInfo](apple_events/1556393-kaeinfo.md)
- [kAEInternetSuite](apple_events/1556388-kaeinternetsuite.md)
- [kAELogOut](apple_events/1556395-kaelogout.md)
- [kAEMenuClass](apple_events/1556392-kaemenuclass.md)
- [kAEMouseClass](apple_events/1556409-kaemouseclass.md)
- [kAENonmodifiable](apple_events/1556386-kaenonmodifiable.md)
- [kAEQDNotOr](apple_events/1556377-kaeqdnotor.md)
- [kAESetPosition](apple_events/1556407-kaesetposition.md)
- [kAESocks4Protocol](apple_events/1542847-kaesocks4protocol.md)
- [kAEUTHasReturningParam](apple_events/1457911-kaeuthasreturningparam.md)
- [kAEUseHTTPProxyAttr](apple_events/1542824-kaeusehttpproxyattr.md)
  Web Services Proxy support—these constants should be added as attributes of the event that is being sent (not as part of the direct object).
- [kAEUseSocksAttr](apple_events/1542933-kaeusesocksattr.md)
- [kAEUserTerminology](apple_events/1457902-kaeuserterminology.md)
- [kAEZoomIn](apple_events/1556365-kaezoomin.md)
- [keyAEAngle](apple_events/1556380-keyaeangle.md)
- [keyAEBaseAddr](apple_events/1556383-keyaebaseaddr.md)
- [keyAEDoScale](apple_events/1556387-keyaedoscale.md)
- [keyAEHiliteRange](apple_events/1556379-keyaehiliterange.md)
- [keyAEKeyword](apple_events/1556374-keyaekeyword.md)
- [keyAESuiteID](apple_events/1556370-keyaesuiteid.md)
- [keyMenuID](apple_events/1556381-keymenuid.md)
- [keyMiscellaneous](apple_events/1556399-keymiscellaneous.md)
- [keyReplyPortAttr](apple_events/1571648-keyreplyportattr.md)
- [keySOAPStructureMetaData](apple_events/1542797-keysoapstructuremetadata.md)
- [keyUserNameAttr](apple_events/1542780-keyusernameattr.md)
- [Apple Event Recording Event ID Constants](apple_events/1527224-apple_event_recording_event_id_c.md)
  Specify event IDs for events that deal with Apple event recording.
- [Callback Constants for the AEResolve Function](apple_events/1572741-callback_constants_for_the_aeres.md)
  Specify supported callback features to the `AEResolve` function.
- [Constants for Object Specifiers, Positions, and Logical and Comparison Operations](apple_events/1572744-constants_for_object_specifiers_.md)
  Specify the types of the four keyword-specified descriptors that make up the data in an object specifier, as well as constants for position, logical operations, and comparison operations.
- [Data Array Constants](apple_events/1542848-data_array_constants.md)
  Specify an array type for storing or extracting descriptor lists with the `AEPutArray` and `AEGetArray` functions.
- [Descriptor Type Constants](apple_events/1542788-descriptor_type_constants.md)
  Specify types for descriptors.
- [Event Class Constants](apple_events/1527210-event_class_constants.md)
  Specify the event class for an Apple event.
- [Event ID Constants](apple_events/1527223-event_id_constants.md)
  Specify the event ID for an Apple event.
- [Event Source Constants](apple_events/1527201-event_source_constants.md)
  Identify how an Apple event was delivered.
- [Factoring Constants](apple_events/1542928-factoring_constants.md)
- [ID Constants for the AECreateAppleEvent Function](apple_events/1542799-id_constants_for_the_aecreateapp.md)
  Specify values for the ID parameters of the `AECreateAppleEvent` function.
- [Key Form and Descriptor Type Object Specifier Constants](apple_events/1572731-key_form_and_descriptor_type_obj.md)
  Specify possible values for the `keyAEKeyForm` field of an object specifier, as well as descriptor types used in resolving object specifiers.
- [Keyword Attribute Constants](apple_events/1542920-keyword_attribute_constants.md)
  Specify keyword values for Apple event attributes.
- [Keyword Parameter Constants](apple_events/1527206-keyword_parameter_constants.md)
  Specify keyword values for Apple event parameters, as well as information for the `AEManagerInfo` function to retrieve. Some common key word values are shown here.
- [Launch Apple Event Constants](apple_events/1556410-launch_apple_event_constants.md)
  In a `kAEOpenApplication` event, specify information about how the receiving application was launched.
- [Numeric Descriptor Type Constants](apple_events/1542872-numeric_descriptor_type_constant.md)
  Specify types for numeric descriptors.
- [Object Class ID Constants](apple_events/1556368-object_class_id_constants.md)
  Specify the object class for an Apple event object.
- [Other Descriptor Type Constants](apple_events/1542760-other_descriptor_type_constants.md)
  Specify types for Boolean and character descriptors.
- [Priority Constants for the AESend Function (Deprecated in macOS)](apple_events/1542840-priority_constants_for_the_aesen.md)
  Specify a value for the `sendPriority` parameter of the `AESend` function.
- [Special Handler Callback Constants](apple_events/1572726-special_handler_callback_constan.md)
  Specify an object callback function to install, get, or remove from the special handler dispatch table.
- [Timeout Constants](apple_events/1542814-timeout_constants.md)
  Specify a timeout value.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/apple_events)*