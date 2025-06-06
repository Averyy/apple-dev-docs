# Carbon Core Functions

**Framework**: Core Services

## Topics

### Functions
- [func AcquireIconRef(IconRef!) -> OSErr](1441852-acquireiconref.md)
- [func CompositeIconRef(IconRef!, IconRef!, UnsafeMutablePointer<IconRef?>!) -> OSErr](1450541-compositeiconref.md)
- [func CreateCompDescriptor(DescType, UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1449155-createcompdescriptor.md)
  Creates a comparison descriptor that specifies how to compare one or more Apple event objects with either another Apple event object or a descriptor.
- [func CreateLogicalDescriptor(UnsafeMutablePointer<AEDescList>!, DescType, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1445212-createlogicaldescriptor.md)
  Creates a logical descriptor that specifies a logical operator and one or more logical terms for the Apple Event Manager to evaluate. 
- [func CreateObjSpecifier(DescType, UnsafeMutablePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1450244-createobjspecifier.md)
  Assembles an object specifier that identifies one or more Apple event objects, from other descriptors.
- [func CreateOffsetDescriptor(Int, UnsafeMutablePointer<AEDesc>!) -> OSErr](1444957-createoffsetdescriptor.md)
  Creates an offset descriptor that specifies the position of an element in relation to the beginning or end of its container. 
- [func CreateRangeDescriptor(UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, Bool, UnsafeMutablePointer<AEDesc>!) -> OSErr](1444087-createrangedescriptor.md)
  Creates a range descriptor that specifies a series of consecutive elements in the same container. 
- [func DCSCopyTextDefinition(DCSDictionary?, CFString, CFRange) -> Unmanaged<CFString>?](1446842-dcscopytextdefinition.md)
  Returns the definition associated with the provided text range.
- [func DCSGetTermRangeInString(DCSDictionary?, CFString, CFIndex) -> CFRange](1450556-dcsgettermrangeinstring.md)
  Determines the range of the longest word or phrase with respect to an offset.
- [func DisposeAECoerceDescUPP(AECoerceDescUPP!)](1448721-disposeaecoercedescupp.md)
  Disposes of a universal procedure pointer to a function that coerces data stored in a descriptor.
- [func DisposeAECoercePtrUPP(AECoercePtrUPP!)](1450664-disposeaecoerceptrupp.md)
  Disposes of a universal procedure pointer to a function that coerces data stored in a buffer.
- [func DisposeAEDisposeExternalUPP(AEDisposeExternalUPP!)](1447284-disposeaedisposeexternalupp.md)
  Disposes of a universal procedure pointer to a function that disposes of data supplied to the `AECreateDescFromExternalPtr` function.
- [func DisposeAEEventHandlerUPP(AEEventHandlerUPP!)](1442066-disposeaeeventhandlerupp.md)
  Disposes of a universal procedure pointer to an event handler function.
- [func DisposeIndexToUCStringUPP(IndexToUCStringUPP!)](1390390-disposeindextoucstringupp.md)
- [func DisposeOSLAccessorUPP(OSLAccessorUPP!)](1444684-disposeoslaccessorupp.md)
  Disposes of a universal procedure pointer to an object accessor function.
- [func DisposeOSLAdjustMarksUPP(OSLAdjustMarksUPP!)](1443940-disposeosladjustmarksupp.md)
  Disposes of a universal procedure pointer to an object callback adjust marks function.
- [func DisposeOSLCompareUPP(OSLCompareUPP!)](1448398-disposeoslcompareupp.md)
  Disposes of a universal procedure pointer to an object callback comparison function.
- [func DisposeOSLCountUPP(OSLCountUPP!)](1443984-disposeoslcountupp.md)
  Disposes of a universal procedure pointer to an object callback count function.
- [func DisposeOSLDisposeTokenUPP(OSLDisposeTokenUPP!)](1442670-disposeosldisposetokenupp.md)
  Disposes of a universal procedure pointer to an object callback dispose token function.
- [func DisposeOSLGetErrDescUPP(OSLGetErrDescUPP!)](1446061-disposeoslgeterrdescupp.md)
  Disposes of a universal procedure pointer to an object callback get error descriptor function.
- [func DisposeOSLGetMarkTokenUPP(OSLGetMarkTokenUPP!)](1442377-disposeoslgetmarktokenupp.md)
  Disposes of a universal procedure pointer to an object callback get mark function.
- [func DisposeOSLMarkUPP(OSLMarkUPP!)](1449253-disposeoslmarkupp.md)
  Disposes of a universal procedure pointer to an object callback mark function.
- [func GetCustomIconsEnabled(Int16, UnsafeMutablePointer<DarwinBoolean>!) -> OSErr](1442255-getcustomiconsenabled.md)
- [func GetIconRef(Int16, OSType, OSType, UnsafeMutablePointer<IconRef?>!) -> OSErr](1442776-geticonref.md)
- [func GetIconRefFromFileInfo(UnsafePointer<FSRef>!, Int, UnsafePointer<UniChar>!, FSCatalogInfoBitmap, UnsafePointer<FSCatalogInfo>!, IconServicesUsageFlags, UnsafeMutablePointer<IconRef?>!, UnsafeMutablePointer<Int16>!) -> OSStatus](1447966-geticonreffromfileinfo.md)
- [func GetIconRefFromFolder(Int16, Int32, Int32, Int8, Int8, UnsafeMutablePointer<IconRef?>!) -> OSErr](1441712-geticonreffromfolder.md)
- [func GetIconRefFromIconFamilyPtr(UnsafePointer<IconFamilyResource>!, Size, UnsafeMutablePointer<IconRef?>!) -> OSStatus](1443251-geticonreffromiconfamilyptr.md)
- [func GetIconRefFromTypeInfo(OSType, OSType, CFString!, CFString!, IconServicesUsageFlags, UnsafeMutablePointer<IconRef?>!) -> OSErr](1445758-geticonreffromtypeinfo.md)
- [func GetIconRefOwners(IconRef!, UnsafeMutablePointer<UInt16>!) -> OSErr](1447221-geticonrefowners.md)
- [func InvokeAECoerceDescUPP(UnsafePointer<AEDesc>!, DescType, SRefCon!, UnsafeMutablePointer<AEDesc>!, AECoerceDescUPP!) -> OSErr](1445450-invokeaecoercedescupp.md)
  Calls a universal procedure pointer to a function that coerces data stored in a descriptor.
- [func InvokeAECoercePtrUPP(DescType, UnsafeRawPointer!, Size, DescType, SRefCon!, UnsafeMutablePointer<AEDesc>!, AECoercePtrUPP!) -> OSErr](1447079-invokeaecoerceptrupp.md)
  Calls a universal procedure pointer to a function that coerces data stored in a buffer.
- [func InvokeAEDisposeExternalUPP(UnsafeRawPointer!, Size, SRefCon!, AEDisposeExternalUPP!)](1441717-invokeaedisposeexternalupp.md)
  Calls a dispose external universal procedure pointer.
- [func InvokeAEEventHandlerUPP(UnsafePointer<AppleEvent>!, UnsafeMutablePointer<AppleEvent>!, SRefCon!, AEEventHandlerUPP!) -> OSErr](1446585-invokeaeeventhandlerupp.md)
  Calls an event handler universal procedure pointer.
- [func InvokeIndexToUCStringUPP(UInt32, UnsafeMutableRawPointer!, UnsafeMutableRawPointer!, UnsafeMutablePointer<Unmanaged<CFString>?>!, UnsafeMutablePointer<UCTypeSelectOptions>!, IndexToUCStringUPP!) -> Bool](1390660-invokeindextoucstringupp.md)
- [func InvokeOSLAccessorUPP(DescType, UnsafePointer<AEDesc>!, DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<AEDesc>!, SRefCon!, OSLAccessorUPP!) -> OSErr](1448978-invokeoslaccessorupp.md)
  Calls an object accessor universal procedure pointer.
- [func InvokeOSLAdjustMarksUPP(Int, Int, UnsafePointer<AEDesc>!, OSLAdjustMarksUPP!) -> OSErr](1448506-invokeosladjustmarksupp.md)
  Calls an object callback adjust marks universal procedure pointer.
- [func InvokeOSLCompareUPP(DescType, UnsafePointer<AEDesc>!, UnsafePointer<AEDesc>!, UnsafeMutablePointer<DarwinBoolean>!, OSLCompareUPP!) -> OSErr](1443110-invokeoslcompareupp.md)
  Calls an object callback comparison universal procedure pointer.
- [func InvokeOSLCountUPP(DescType, DescType, UnsafePointer<AEDesc>!, UnsafeMutablePointer<Int>!, OSLCountUPP!) -> OSErr](1448030-invokeoslcountupp.md)
  Calls an object callback count universal procedure pointer.
- [func InvokeOSLDisposeTokenUPP(UnsafeMutablePointer<AEDesc>!, OSLDisposeTokenUPP!) -> OSErr](1443963-invokeosldisposetokenupp.md)
  Calls an object callback dispose token universal procedure pointer.
- [func InvokeOSLGetErrDescUPP(UnsafeMutablePointer<UnsafeMutablePointer<AEDesc>?>!, OSLGetErrDescUPP!) -> OSErr](1448420-invokeoslgeterrdescupp.md)
  Calls an object callback get error descriptor universal procedure pointer.
- [func InvokeOSLGetMarkTokenUPP(UnsafePointer<AEDesc>!, DescType, UnsafeMutablePointer<AEDesc>!, OSLGetMarkTokenUPP!) -> OSErr](1441894-invokeoslgetmarktokenupp.md)
  Calls an object callback get mark universal procedure pointer.
- [func InvokeOSLMarkUPP(UnsafePointer<AEDesc>!, UnsafePointer<AEDesc>!, Int, OSLMarkUPP!) -> OSErr](1447444-invokeoslmarkupp.md)
  Calls an object callback mark universal procedure pointer.
- [func IsDataAvailableInIconRef(OSType, IconRef!) -> Bool](1446627-isdataavailableiniconref.md)
- [func IsIconRefComposite(IconRef!, UnsafeMutablePointer<IconRef?>!, UnsafeMutablePointer<IconRef?>!) -> OSErr](1446300-isiconrefcomposite.md)
- [func IsValidIconRef(IconRef!) -> Bool](1450233-isvalidiconref.md)
- [func LSSetItemAttribute(UnsafePointer<FSRef>!, LSRolesMask, CFString!, CFTypeRef!) -> OSStatus](1446733-lssetitemattribute.md)
- [func LSSharedFileListAddObserver(LSSharedFileList?, CFRunLoop, CFString, LSSharedFileListChangedProcPtr, UnsafeMutableRawPointer?)](1445770-lssharedfilelistaddobserver.md)
- [func LSSharedFileListCopyProperty(LSSharedFileList, CFString) -> Unmanaged<CFTypeRef>?](1444588-lssharedfilelistcopyproperty.md)
- [func LSSharedFileListCopySnapshot(LSSharedFileList, UnsafeMutablePointer<UInt32>?) -> Unmanaged<CFArray>?](1448112-lssharedfilelistcopysnapshot.md)
- [func LSSharedFileListCreate(CFAllocator?, CFString, CFTypeRef?) -> Unmanaged<LSSharedFileList>?](1443926-lssharedfilelistcreate.md)
- [func LSSharedFileListGetSeedValue(LSSharedFileList) -> UInt32](1444885-lssharedfilelistgetseedvalue.md)
- [func LSSharedFileListGetTypeID() -> CFTypeID](1450618-lssharedfilelistgettypeid.md)
- [func LSSharedFileListInsertItemFSRef(LSSharedFileList, LSSharedFileListItem, CFString?, IconRef?, UnsafePointer<FSRef>, CFDictionary?, CFArray?) -> LSSharedFileListItem?](1449884-lssharedfilelistinsertitemfsref.md)
- [func LSSharedFileListInsertItemURL(LSSharedFileList, LSSharedFileListItem, CFString?, IconRef?, CFURL, CFDictionary?, CFArray?) -> LSSharedFileListItem?](1444471-lssharedfilelistinsertitemurl.md)
- [func LSSharedFileListItemCopyDisplayName(LSSharedFileListItem) -> Unmanaged<CFString>](1449716-lssharedfilelistitemcopydisplayn.md)
- [func LSSharedFileListItemCopyIconRef(LSSharedFileListItem) -> IconRef](1442889-lssharedfilelistitemcopyiconref.md)
- [func LSSharedFileListItemCopyProperty(LSSharedFileListItem, CFString) -> Unmanaged<CFTypeRef>?](1445074-lssharedfilelistitemcopyproperty.md)
- [func LSSharedFileListItemCopyResolvedURL(LSSharedFileListItem, LSSharedFileListResolutionFlags, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>?](1449882-lssharedfilelistitemcopyresolved.md)
- [func LSSharedFileListItemGetID(LSSharedFileListItem) -> UInt32](1443305-lssharedfilelistitemgetid.md)
- [func LSSharedFileListItemGetTypeID() -> CFTypeID](1447138-lssharedfilelistitemgettypeid.md)
- [func LSSharedFileListItemMove(LSSharedFileList, LSSharedFileListItem, LSSharedFileListItem) -> OSStatus](1444348-lssharedfilelistitemmove.md)
- [func LSSharedFileListItemRemove(LSSharedFileList, LSSharedFileListItem) -> OSStatus](1442025-lssharedfilelistitemremove.md)
- [func LSSharedFileListItemResolve(LSSharedFileListItem, LSSharedFileListResolutionFlags, UnsafeMutablePointer<Unmanaged<CFURL>?>?, UnsafeMutablePointer<FSRef>?) -> OSStatus](1447347-lssharedfilelistitemresolve.md)
- [func LSSharedFileListItemSetProperty(LSSharedFileListItem, CFString, CFTypeRef) -> OSStatus](1445766-lssharedfilelistitemsetproperty.md)
- [func LSSharedFileListRemoveAllItems(LSSharedFileList) -> OSStatus](1446389-lssharedfilelistremoveallitems.md)
- [func LSSharedFileListRemoveObserver(LSSharedFileList, CFRunLoop, CFString, LSSharedFileListChangedProcPtr, UnsafeMutableRawPointer?)](1443404-lssharedfilelistremoveobserver.md)
- [func LSSharedFileListSetAuthorization(LSSharedFileList, AuthorizationRef) -> OSStatus](1446834-lssharedfilelistsetauthorization.md)
- [func LSSharedFileListSetProperty(LSSharedFileList, CFString, CFTypeRef?) -> OSStatus](1448857-lssharedfilelistsetproperty.md)
- [func MDCopyLabelKinds() -> CFArray!](1442887-mdcopylabelkinds.md)
- [func MDCopyLabelWithUUID(CFUUID!) -> MDLabel!](1447030-mdcopylabelwithuuid.md)
- [func MDCopyLabelsMatchingExpression(CFString!) -> CFArray!](1448237-mdcopylabelsmatchingexpression.md)
- [func MDCopyLabelsWithKind(CFString!) -> CFArray!](1444230-mdcopylabelswithkind.md)
- [func MDItemCopyLabels(MDItem!) -> CFArray!](1442606-mditemcopylabels.md)
- [func MDItemRemoveLabel(MDItem!, MDLabel!) -> Bool](1446067-mditemremovelabel.md)
- [func MDItemSetLabel(MDItem!, MDLabel!) -> Bool](1442559-mditemsetlabel.md)
- [func MDItemsCopyAttributes(CFArray!, CFArray!) -> CFArray!](1426975-mditemscopyattributes.md)
- [func MDItemsCreateWithURLs(CFAllocator!, CFArray!) -> CFArray!](1427086-mditemscreatewithurls.md)
- [func MDLabelCopyAttribute(MDLabel!, CFString!) -> CFTypeRef!](1445456-mdlabelcopyattribute.md)
- [func MDLabelCopyAttributeName(MDLabel!) -> CFString!](1445522-mdlabelcopyattributename.md)
- [func MDLabelCreate(CFAllocator!, CFString!, CFString!, MDLabelDomain) -> MDLabel!](1442614-mdlabelcreate.md)
- [func MDLabelDelete(MDLabel!) -> Bool](1449203-mdlabeldelete.md)
- [func MDLabelGetTypeID() -> CFTypeID](1446579-mdlabelgettypeid.md)
- [func MDLabelSetAttributes(MDLabel!, CFDictionary!) -> Bool](1449005-mdlabelsetattributes.md)
- [func MDQueryCreateForItems(CFAllocator!, CFString!, CFArray!, CFArray!, CFArray!) -> MDQuery!](1413031-mdquerycreateforitems.md)
- [func MDQueryGetSortOptionFlagsForAttribute(MDQuery!, CFString!) -> UInt32](1413013-mdquerygetsortoptionflagsforattr.md)
- [func MDQuerySetSortOptionFlagsForAttribute(MDQuery!, CFString!, UInt32) -> Bool](1413075-mdquerysetsortoptionflagsforattr.md)
- [func MDQuerySetSortOrder(MDQuery!, CFArray!) -> Bool](1413096-mdquerysetsortorder.md)
- [func NewAECoerceDescUPP(AECoerceDescProcPtr!) -> AECoerceDescUPP!](1445885-newaecoercedescupp.md)
  Creates a new universal procedure pointer to a function that coerces data stored in a descriptor.
- [func NewAECoercePtrUPP(AECoercePtrProcPtr!) -> AECoercePtrUPP!](1449962-newaecoerceptrupp.md)
  Creates a new universal procedure pointer to a function that coerces data stored in a buffer.
- [func NewAEDisposeExternalUPP(AEDisposeExternalProcPtr!) -> AEDisposeExternalUPP!](1447774-newaedisposeexternalupp.md)
  Creates a new universal procedure pointer to a function that disposes of data stored in a buffer.
- [func NewAEEventHandlerUPP(AEEventHandlerProcPtr!) -> AEEventHandlerUPP!](1446862-newaeeventhandlerupp.md)
  Creates a new universal procedure pointer to an event handler function.
- [func NewIndexToUCStringUPP(IndexToUCStringProcPtr!) -> IndexToUCStringUPP!](1390384-newindextoucstringupp.md)
- [func NewOSLAccessorUPP(OSLAccessorProcPtr!) -> OSLAccessorUPP!](1449584-newoslaccessorupp.md)
  Creates a new universal procedure pointer to an object accessor function.
- [func NewOSLAdjustMarksUPP(OSLAdjustMarksProcPtr!) -> OSLAdjustMarksUPP!](1443347-newosladjustmarksupp.md)
  Creates a new universal procedure pointer to an object callback adjust marks function.
- [func NewOSLCompareUPP(OSLCompareProcPtr!) -> OSLCompareUPP!](1444603-newoslcompareupp.md)
  Creates a new universal procedure pointer to an object callback comparison function.
- [func NewOSLCountUPP(OSLCountProcPtr!) -> OSLCountUPP!](1448156-newoslcountupp.md)
  Creates a new universal procedure pointer to an object callback count function.
- [func NewOSLDisposeTokenUPP(OSLDisposeTokenProcPtr!) -> OSLDisposeTokenUPP!](1450027-newosldisposetokenupp.md)
  Creates a new universal procedure pointer to an object callback dispose token function.
- [func NewOSLGetErrDescUPP(OSLGetErrDescProcPtr!) -> OSLGetErrDescUPP!](1447934-newoslgeterrdescupp.md)
  Creates a new universal procedure pointer to an object callback get error descriptor function.
- [func NewOSLGetMarkTokenUPP(OSLGetMarkTokenProcPtr!) -> OSLGetMarkTokenUPP!](1445166-newoslgetmarktokenupp.md)
  Creates a new universal procedure pointer to an object callback get mark function.
- [func NewOSLMarkUPP(OSLMarkProcPtr!) -> OSLMarkUPP!](1446942-newoslmarkupp.md)
  Creates a new universal procedure pointer to an object callback mark function.
- [func OverrideIconRef(IconRef!, IconRef!) -> OSErr](1445253-overrideiconref.md)
- [func ReadIconFromFSRef(UnsafePointer<FSRef>!, UnsafeMutablePointer<IconFamilyHandle?>!) -> OSStatus](1444939-readiconfromfsref.md)
- [func RegisterIconRefFromFSRef(OSType, OSType, UnsafePointer<FSRef>!, UnsafeMutablePointer<IconRef?>!) -> OSStatus](1446795-registericonreffromfsref.md)
- [func RegisterIconRefFromIconFamily(OSType, OSType, IconFamilyHandle!, UnsafeMutablePointer<IconRef?>!) -> OSErr](1443918-registericonreffromiconfamily.md)
- [func ReleaseIconRef(IconRef!) -> OSErr](1443504-releaseiconref.md)
- [func RemoveIconRefOverride(IconRef!) -> OSErr](1445832-removeiconrefoverride.md)
- [func SetCustomIconsEnabled(Int16, Bool) -> OSErr](1449302-setcustomiconsenabled.md)
- [func UCTypeSelectAddKeyToSelector(UCTypeSelectRef!, CFString!, Double, UnsafeMutablePointer<DarwinBoolean>!) -> OSStatus](1390517-uctypeselectaddkeytoselector.md)
- [func UCTypeSelectCompare(UCTypeSelectRef!, CFString!, UnsafeMutablePointer<UCTypeSelectCompareResult>!) -> OSStatus](1390474-uctypeselectcompare.md)
- [func UCTypeSelectCreateSelector(LocaleRef!, LocaleOperationVariant, UCCollateOptions, UnsafeMutablePointer<UCTypeSelectRef?>!) -> OSStatus](1390445-uctypeselectcreateselector.md)
- [func UCTypeSelectFindItem(UCTypeSelectRef!, UInt32, UnsafeMutableRawPointer!, UnsafeMutableRawPointer!, IndexToUCStringUPP!, UnsafeMutablePointer<UInt32>!) -> OSStatus](1390368-uctypeselectfinditem.md)
- [func UCTypeSelectFlushSelectorData(UCTypeSelectRef!) -> OSStatus](1390367-uctypeselectflushselectordata.md)
- [func UCTypeSelectReleaseSelector(UnsafeMutablePointer<UCTypeSelectRef?>!) -> OSStatus](1390644-uctypeselectreleaseselector.md)
- [func UCTypeSelectWalkList(UCTypeSelectRef!, CFString!, UCTSWalkDirection, UInt32, UnsafeMutableRawPointer!, UnsafeMutableRawPointer!, IndexToUCStringUPP!, UnsafeMutablePointer<UInt32>!) -> OSStatus](1390442-uctypeselectwalklist.md)
- [func UCTypeSelectWouldResetBuffer(UCTypeSelectRef!, CFString!, Double) -> Bool](1390538-uctypeselectwouldresetbuffer.md)
- [func UTCreateStringForOSType(OSType) -> Unmanaged<CFString>](1442804-utcreatestringforostype.md)
  Encodes an `OSType` into a string suitable for use as a tag argument.
- [func UTGetOSTypeFromString(CFString) -> OSType](1450472-utgetostypefromstring.md)
  Decodes a tag string into an OSType.
- [func UTTypeConformsTo(CFString, CFString) -> Bool](1444079-uttypeconformsto.md)
  Returns whether a uniform type identifier conforms to another uniform type identifier.
- [func UTTypeCopyAllTagsWithClass(CFString, CFString) -> Unmanaged<CFArray>?](1448473-uttypecopyalltagswithclass.md)
- [func UTTypeCopyDeclaration(CFString) -> Unmanaged<CFDictionary>?](1442505-uttypecopydeclaration.md)
  Returns a uniform type’s declaration.
- [func UTTypeCopyDeclaringBundleURL(CFString) -> Unmanaged<CFURL>?](1447781-uttypecopydeclaringbundleurl.md)
  Returns the location of a bundle containing the declaration for a type.
- [func UTTypeCopyDescription(CFString) -> Unmanaged<CFString>?](1448514-uttypecopydescription.md)
  Returns the localized, user-readable type description string associated with a uniform type identifier.
- [func UTTypeCopyPreferredTagWithClass(CFString, CFString) -> Unmanaged<CFString>?](1442744-uttypecopypreferredtagwithclass.md)
  Translates a uniform type identifier to a list of tags in a different type classification method.
- [func UTTypeCreateAllIdentifiersForTag(CFString, CFString, CFString?) -> Unmanaged<CFArray>?](1447261-uttypecreateallidentifiersfortag.md)
  Creates an array of all uniform type identifiers for the type indicated by the specified tag.
- [func UTTypeCreatePreferredIdentifierForTag(CFString, CFString, CFString?) -> Unmanaged<CFString>?](1448939-uttypecreatepreferredidentifierf.md)
  Creates a uniform type identifier for the type indicated by the specified tag.
- [func UTTypeEqual(CFString, CFString) -> Bool](1447783-uttypeequal.md)
  Returns whether two uniform type identifiers are equal.
- [func UTTypeIsDeclared(CFString) -> Bool](1450352-uttypeisdeclared.md)
- [func UTTypeIsDynamic(CFString) -> Bool](1442980-uttypeisdynamic.md)
- [func UnregisterIconRef(OSType, OSType) -> OSErr](1444660-unregistericonref.md)
- [func UpdateIconRef(IconRef!) -> OSErr](1445921-updateiconref.md)
- [func vAEBuildAppleEvent(AEEventClass, AEEventID, DescType, UnsafeRawPointer!, Size, Int16, Int32, UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](1441729-vaebuildappleevent.md)
  Allows you to encapsulate calls to `AEBuildAppleEvent` in a wrapper routine.
- [func vAEBuildDesc(UnsafeMutablePointer<AEDesc>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](1446775-vaebuilddesc.md)
  Allows you to encapsulate calls to `AEBuildDesc` in your own wrapper routines.
- [func vAEBuildParameters(UnsafeMutablePointer<AppleEvent>!, UnsafeMutablePointer<AEBuildError>!, UnsafePointer<CChar>!, CVaListPointer) -> OSStatus](1448040-vaebuildparameters.md)
  Allows you to encapsulate calls to `AEBuildParameters` in your own `stdarg`-style wrapper routines, using techniques similar to those allowed by vsprintf.
- [func AEDeterminePermissionToAutomateTarget(UnsafePointer<AEAddressDesc>!, AEEventClass, AEEventID, Bool) -> OSStatus](3025784-aedeterminepermissiontoautomatet.md)
- [func AEUnflattenDescFromBytes(UnsafeRawPointer!, Int, UnsafeMutablePointer<AEDesc>!) -> OSStatus](3553279-aeunflattendescfrombytes.md)
- [func MDItemGetCacheFileDescriptors(CFArray!, ((CFArray?) -> Void)!)](4485578-mditemgetcachefiledescriptors.md)

## See Also

- [Carbon Core Structures](carbon_core/carbon_core_structures.md)
- [Carbon Core Enumerations](carbon_core/carbon_core_enumerations.md)
- [Carbon Core Data Types](carbon_core/carbon_core_data_types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/carbon_core_functions)*