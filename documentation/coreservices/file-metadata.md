# File Metadata

**Framework**: Core Services

Search for files based on data that is part of the file or file system.

## Topics

### Opaque Types
- [MDSchema](file_metadata/mdschema.md)
- [MDItem](file_metadata/mditem.md)
### Structures
- [struct MDExporterInterfaceStruct](mdexporterinterfacestruct.md)
- [struct MDImporterBundleWrapperURLInterfaceStruct](mdimporterbundlewrapperurlinterfacestruct.md)
- [struct MDImporterInterfaceStruct](mdimporterinterfacestruct.md)
- [struct MDImporterURLInterfaceStruct](mdimporterurlinterfacestruct.md)
- [struct MDLabelDomain](mdlabeldomain.md)
- [struct MDQuerySortOptionFlags](mdquerysortoptionflags.md)
### Classes
- [class MDLabel](mdlabel.md)
### Data Types
- [MDQuery](file_metadata/mdquery.md)
### Constants
- [let kMDItemApplicationCategories: CFString!](kmditemapplicationcategories.md)
- [let kMDItemCameraOwner: CFString!](kmditemcameraowner.md)
- [let kMDItemContentTypeTree: CFString!](kmditemcontenttypetree.md)
- [let kMDItemDateAdded: CFString!](kmditemdateadded.md)
- [let kMDItemDownloadedDate: CFString!](kmditemdownloadeddate.md)
- [let kMDItemEditors: CFString!](kmditemeditors.md)
- [let kMDItemExecutableArchitectures: CFString!](kmditemexecutablearchitectures.md)
- [let kMDItemExecutablePlatform: CFString!](kmditemexecutableplatform.md)
- [let kMDItemFocalLength35mm: CFString!](kmditemfocallength35mm.md)
- [let kMDItemGPSAreaInformation: CFString!](kmditemgpsareainformation.md)
- [let kMDItemGPSDOP: CFString!](kmditemgpsdop.md)
- [let kMDItemGPSDateStamp: CFString!](kmditemgpsdatestamp.md)
- [let kMDItemGPSDestBearing: CFString!](kmditemgpsdestbearing.md)
- [let kMDItemGPSDestDistance: CFString!](kmditemgpsdestdistance.md)
- [let kMDItemGPSDestLatitude: CFString!](kmditemgpsdestlatitude.md)
- [let kMDItemGPSDestLongitude: CFString!](kmditemgpsdestlongitude.md)
- [let kMDItemGPSDifferental: CFString!](kmditemgpsdifferental.md)
- [let kMDItemGPSMapDatum: CFString!](kmditemgpsmapdatum.md)
- [let kMDItemGPSMeasureMode: CFString!](kmditemgpsmeasuremode.md)
- [let kMDItemGPSProcessingMethod: CFString!](kmditemgpsprocessingmethod.md)
- [let kMDItemGPSStatus: CFString!](kmditemgpsstatus.md)
- [let kMDItemHTMLContent: CFString!](kmditemhtmlcontent.md)
- [let kMDItemIsApplicationManaged: CFString!](kmditemisapplicationmanaged.md)
- [let kMDItemIsLikelyJunk: CFString!](kmditemislikelyjunk.md)
- [let kMDItemLensModel: CFString!](kmditemlensmodel.md)
- [let kMDLabelAddedNotification: CFString!](kmdlabeladdednotification.md)
- [var kMDLabelBundleURL: Unmanaged<CFString>!](kmdlabelbundleurl.md)
- [let kMDLabelChangedNotification: CFString!](kmdlabelchangednotification.md)
- [var kMDLabelContentChangeDate: Unmanaged<CFString>!](kmdlabelcontentchangedate.md)
- [var kMDLabelDisplayName: Unmanaged<CFString>!](kmdlabeldisplayname.md)
- [var kMDLabelIconData: Unmanaged<CFString>!](kmdlabelicondata.md)
- [var kMDLabelIconUUID: Unmanaged<CFString>!](kmdlabeliconuuid.md)
- [var kMDLabelIsMutuallyExclusiveSetMember: Unmanaged<CFString>!](kmdlabelismutuallyexclusivesetmember.md)
- [var kMDLabelKind: Unmanaged<CFString>!](kmdlabelkind.md)
- [var kMDLabelKindIsMutuallyExclusiveSetKey: Unmanaged<CFString>!](kmdlabelkindismutuallyexclusivesetkey.md)
- [var kMDLabelKindVisibilityKey: Unmanaged<CFString>!](kmdlabelkindvisibilitykey.md)
- [var kMDLabelLocalDomain: MDLabelDomain](kmdlabellocaldomain.md)
- [let kMDLabelRemovedNotification: CFString!](kmdlabelremovednotification.md)
- [var kMDLabelSetsFinderColor: Unmanaged<CFString>!](kmdlabelsetsfindercolor.md)
- [var kMDLabelUUID: Unmanaged<CFString>!](kmdlabeluuid.md)
- [var kMDLabelUserDomain: MDLabelDomain](kmdlabeluserdomain.md)
- [var kMDLabelVisibility: Unmanaged<CFString>!](kmdlabelvisibility.md)
- [var kMDPrivateVisibility: Unmanaged<CFString>!](kmdprivatevisibility.md)
- [var kMDPublicVisibility: Unmanaged<CFString>!](kmdpublicvisibility.md)
- [var kMDQueryAllowFSTranslation: MDQueryOptionFlags](kmdqueryallowfstranslation.md)
- [var kMDQueryReverseSortOrderFlag: MDQuerySortOptionFlags](kmdqueryreversesortorderflag.md)
- [var kMDQuerySynchronous: MDQueryOptionFlags](kmdquerysynchronous.md)
  Specifies that a query should block during the initial gather phase. The query’s run loop will run in the default mode. If this option is not specified the query function returns immediately after starting the query asynchronously.
- [var kMDQueryWantsUpdates: MDQueryOptionFlags](kmdquerywantsupdates.md)

## See Also

- [File Metadata Search Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/Introduction.html#//apple_ref/doc/uid/TP40001841)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata)*