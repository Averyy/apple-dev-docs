# IODetailedTimingInformationV2

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.1+

## Declaration

```swift
typedef struct IODetailedTimingInformationV2 IODetailedTimingInformationV2;
```

## Topics

### Instance Properties
- [horizontalActive](iodetailedtiminginformationv2/1386525-horizontalactive.md)
  Pixel clocks per line.
- [horizontalBlanking](iodetailedtiminginformationv2/1386867-horizontalblanking.md)
  Blanking clocks per line.
- [horizontalBorderLeft](iodetailedtiminginformationv2/1386910-horizontalborderleft.md)
  Number of pixels in left horizontal border.
- [horizontalBorderRight](iodetailedtiminginformationv2/1386906-horizontalborderright.md)
  Number of pixels in right horizontal border.
- [horizontalScaled](iodetailedtiminginformationv2/1386940-horizontalscaled.md)
  If the mode is scaled, sets the size of the image before scaling or rotation.
- [horizontalScaledInset](iodetailedtiminginformationv2/1386630-horizontalscaledinset.md)
  If the mode is scaled, sets the number of active pixels to remove the left and right edges in order to display an underscanned image.
- [horizontalSyncConfig](iodetailedtiminginformationv2/1386197-horizontalsyncconfig.md)
  kIOSyncPositivePolarity for positive polarity horizontal sync (0 for negative).
- [horizontalSyncLevel](iodetailedtiminginformationv2/1386460-horizontalsynclevel.md)
  Zero.
- [horizontalSyncOffset](iodetailedtiminginformationv2/1386455-horizontalsyncoffset.md)
  First clock of horizontal sync.
- [horizontalSyncPulseWidth](iodetailedtiminginformationv2/1385903-horizontalsyncpulsewidth.md)
  Width of horizontal sync.
- [maxPixelClock](iodetailedtiminginformationv2/1386256-maxpixelclock.md)
  Maximum pixel clock frequency in Hz, with error.
- [minPixelClock](iodetailedtiminginformationv2/1385762-minpixelclock.md)
  Minimum pixel clock frequency in Hz, with error.
- [numLinks](iodetailedtiminginformationv2/1386401-numlinks.md)
  number of links to be used by a dual link timing, if zero, assume one link.
- [pixelClock](iodetailedtiminginformationv2/1385975-pixelclock.md)
  Pixel clock frequency in Hz.
- [scalerFlags](iodetailedtiminginformationv2/1386950-scalerflags.md)
  If the mode is scaled, kIOScaleStretchToFit may be set to allow stretching. kIOScaleRotateFlags is mask which may have the value given by kIOScaleRotate90, kIOScaleRotate180, kIOScaleRotate270 to display a rotated framebuffer.
- [signalConfig](iodetailedtiminginformationv2/1386578-signalconfig.md)
  kIOAnalogSetupExpected set if display expects a blank-to-black setup or pedestal. See VESA signal standards.
- [signalLevels](iodetailedtiminginformationv2/1386883-signallevels.md)
  One of:
- [verticalActive](iodetailedtiminginformationv2/1386920-verticalactive.md)
  Number of lines per frame.
- [verticalBlanking](iodetailedtiminginformationv2/1386655-verticalblanking.md)
  Blanking lines per frame.
- [verticalBorderBottom](iodetailedtiminginformationv2/1386527-verticalborderbottom.md)
  Number of lines in bottom vertical border.
- [verticalBorderTop](iodetailedtiminginformationv2/1386386-verticalbordertop.md)
  Number of lines in top vertical border.
- [verticalScaled](iodetailedtiminginformationv2/1386813-verticalscaled.md)
  If the mode is scaled, sets the size of the image before scaling or rotation.
- [verticalScaledInset](iodetailedtiminginformationv2/1386086-verticalscaledinset.md)
  If the mode is scaled, sets the number of active lines to remove the top and bottom edges in order to display an underscanned image.
- [verticalSyncConfig](iodetailedtiminginformationv2/1385877-verticalsyncconfig.md)
  kIOSyncPositivePolarity for positive polarity vertical sync (0 for negative).
- [verticalSyncLevel](iodetailedtiminginformationv2/1386863-verticalsynclevel.md)
  Zero.
- [verticalSyncOffset](iodetailedtiminginformationv2/1386497-verticalsyncoffset.md)
  First line of vertical sync.
- [verticalSyncPulseWidth](iodetailedtiminginformationv2/1385779-verticalsyncpulsewidth.md)
  Height of vertical sync.
- [bitsPerColorComponent](iodetailedtiminginformationv2/2937381-bitspercolorcomponent.md)
- [colorimetry](iodetailedtiminginformationv2/2937389-colorimetry.md)
- [dscCompressedBitsPerPixel](iodetailedtiminginformationv2/3131500-dsccompressedbitsperpixel.md)
- [dscSliceHeight](iodetailedtiminginformationv2/3131501-dscsliceheight.md)
- [dscSliceWidth](iodetailedtiminginformationv2/3131502-dscslicewidth.md)
- [dynamicRange](iodetailedtiminginformationv2/2937358-dynamicrange.md)
- [pixelEncoding](iodetailedtiminginformationv2/2937412-pixelencoding.md)
- [verticalBlankingExtension](iodetailedtiminginformationv2/2869555-verticalblankingextension.md)
- [verticalBlankingMaxShrinkPerFrame](iodetailedtiminginformationv2/3753513-verticalblankingmaxshrinkperfram.md)
- [verticalBlankingMaxStretchPerFrame](iodetailedtiminginformationv2/3753514-verticalblankingmaxstretchperfra.md)

## See Also

- [IOAccelBounds](ioaccelbounds.md)
- [IOAccelDeviceRegion](ioacceldeviceregion.md)
- [IOAccelID](ioaccelid.md)
- [IOAccelSize](ioaccelsize.md)
- [IOAccelSurfaceInformation](ioaccelsurfaceinformation.md)
- [IOAccelSurfaceReadData](ioaccelsurfacereaddata.md)
- [IOAccelSurfaceScaling](ioaccelsurfacescaling.md)
- [IOAddressRange](ioaddressrange.md)
- [IOAddressSegment](ioaddresssegment.md)
- [IOAlignment](ioalignment.md)
- [IOAppleTimingID](ioappletimingid.md)
- [IOAsyncMethod](ioasyncmethod.md)
- [IOBlockStorageDeviceExtent](ioblockstoragedeviceextent.md)
  Extent for unmap storage requests.
- [IOBlockStorageProvisionDeviceExtent](ioblockstorageprovisiondeviceextent.md)
- [IOByteCount](iobytecount.md)
- [IOByteCount32](iobytecount32.md)
- [IOByteCount64](iobytecount64.md)
- [IOCSRKeyType](iocsrkeytype.md)
- [IOCacheMode](iocachemode.md)
- [IOColorComponent](iocolorcomponent.md)
- [IOColorEntry](iocolorentry.md)
- [IOCommandCode](iocommandcode.md)
- [IOCommandID](iocommandid.md)
- [IOCommandKind](iocommandkind.md)
- [IOConfigKeyType](ioconfigkeytype.md)
- [IODMAMapPageList](iodmamappagelist.md)
- [IODMAMapSpecification](iodmamapspecification.md)
- [IODTCompareAddressCellFunc](iodtcompareaddresscellfunc.md)
- [IODTNVLocationFunc](iodtnvlocationfunc.md)
- [IODataQueueClientDequeueEntryBlock](iodataqueueclientdequeueentryblock.md)
- [IODataQueueClientEnqueueEntryBlock](iodataqueueclientenqueueentryblock.md)
- [IODebuggerLinkStatusHandler](iodebuggerlinkstatushandler.md)
- [IODebuggerRxHandler](iodebuggerrxhandler.md)
- [IODebuggerSetModeHandler](iodebuggersetmodehandler.md)
- [IODebuggerTxHandler](iodebuggertxhandler.md)
- [IODetailedTimingInformation](iodetailedtiminginformation.md)
- [IODetailedTimingInformationV1](iodetailedtiminginformationv1.md)
- [IODispatchBlock](iodispatchblock.md)
- [IODispatchFunction](iodispatchfunction.md)
- [IODispatchLogFunction](iodispatchlogfunction.md)
- [IODispatchQueueCancelHandler](iodispatchqueuecancelhandler.md)
- [IODispatchQueueName](iodispatchqueuename.md)
- [IODispatchSourceCancelHandler](iodispatchsourcecancelhandler.md)
- [IODisplayModeID](iodisplaymodeid.md)
- [IODisplayModeInformation](iodisplaymodeinformation.md)
- [IODisplayProductID](iodisplayproductid.md)
- [IODisplayScalerInformation](iodisplayscalerinformation.md)
- [IODisplayTimingRange](iodisplaytimingrange.md)
- [IODisplayTimingRangeV1](iodisplaytimingrangev1.md)
- [IODisplayTimingRangeV2](iodisplaytimingrangev2.md)
- [IODisplayVendorID](iodisplayvendorid.md)
- [IOEnetMulticastMode](ioenetmulticastmode.md)
- [IOEnetPromiscuousMode](ioenetpromiscuousmode.md)
- [IOEthernetAddress](ioethernetaddress.md)
- [IOExternalAsyncMethod](ioexternalasyncmethod.md)
- [IOExternalMethod](ioexternalmethod.md)
- [IOExternalMethodAction](ioexternalmethodaction.md)
- [IOExternalMethodArguments](ioexternalmethodarguments.md)
- [IOExternalMethodDispatch](ioexternalmethoddispatch.md)
- [IOExternalTrap](ioexternaltrap.md)
- [IOFBCursorRef](iofbcursorref.md)
- [IOFBDPLinkConfig](iofbdplinkconfig.md)
- [IOFBDisplayModeDescription](iofbdisplaymodedescription.md)
- [IOFBHDRMetaData](iofbhdrmetadata.md)
- [IOFBHDRMetaDataV1](iofbhdrmetadatav1.md)
- [IOFBInterruptProc](iofbinterruptproc.md)
- [IOFixed](iofixed.md)
- [IOFixed1616](iofixed1616.md)
- [IOFixedPoint32](iofixedpoint32.md)
- [IOFourCharCode](iofourcharcode.md)
- [IOFramebufferNotificationHandler](ioframebuffernotificationhandler.md)
- [IOFramebufferNotificationNotify](ioframebuffernotificationnotify.md)
- [IOGBounds](iogbounds.md)
- [IOGPoint](iogpoint.md)
- [IOGSize](iogsize.md)
- [IOHardwareCursorDescriptor](iohardwarecursordescriptor.md)
- [IOHardwareCursorInfo](iohardwarecursorinfo.md)
- [IOIndex](ioindex.md)
- [IOInterruptAction](iointerruptaction.md)
- [IOInterruptActionBlock](iointerruptactionblock.md)
- [IOInterruptDispatchSourcePayload](iointerruptdispatchsourcepayload.md)
- [IOInterruptHandler](iointerrupthandler.md)
- [IOInterruptState](iointerruptstate.md)
- [IOInterruptVectorNumber](iointerruptvectornumber.md)
- [IOItemCount](ioitemcount.md)
- [IOLock](iolock.md)
- [IOLogicalAddress](iologicaladdress.md)
- [IOMediaAttributeMask](iomediaattributemask.md)
- [IOMediaState](iomediastate.md)
- [IOMessage](iomessage.md)
- [IOMethod](iomethod.md)
- [IONDRVControlParameters](iondrvcontrolparameters.md)
- [IONVRAMDescriptor](ionvramdescriptor.md)
- [IONamedValue](ionamedvalue.md)
- [IONotificationRef](ionotificationref.md)
- [IOOptionBits](iooptionbits.md)
- [IOOutputAction](iooutputaction.md)
- [IOPCIDeviceConfigHandler](iopcideviceconfighandler.md)
- [IOPCIEvent](iopcievent.md)
- [IOPCIPhysicalAddress](iopciphysicaladdress.md)
- [IOPMCalendarStruct](iopmcalendarstruct.md)
- [IOPMDriverAssertionID](iopmdriverassertionid.md)
- [IOPMDriverAssertionLevel](iopmdriverassertionlevel.md)
- [IOPMDriverAssertionType](iopmdriverassertiontype.md)
- [IOPMSettingControllerCallback](iopmsettingcontrollercallback.md)
- [IOPhysicalAddress](iophysicaladdress.md)
- [IOPhysicalAddress32](iophysicaladdress32.md)
- [IOPhysicalAddress64](iophysicaladdress64.md)
- [IOPhysicalLength](iophysicallength.md)
- [IOPhysicalLength32](iophysicallength32.md)
- [IOPhysicalLength64](iophysicallength64.md)
- [IOPhysicalRange](iophysicalrange.md)
- [IOPixelAperture](iopixelaperture.md)
- [IOPixelEncoding](iopixelencoding.md)
- [IOPixelInformation](iopixelinformation.md)
- [IOPowerStateChangeNotification](iopowerstatechangenotification.md)
- [IOPropertyName](iopropertyname.md)
- [IORPC](iorpc.md)
- [IORPCMessage](iorpcmessage.md)
- [IORPCMessageErrorReturn](iorpcmessageerrorreturn.md)
- [IORPCMessageErrorReturnContent](iorpcmessageerrorreturncontent.md)
- [IORPCMessageMach](iorpcmessagemach.md)
- [IORWLock](iorwlock.md)
- [IORangeScalar](iorangescalar.md)
- [IORecursiveLock](iorecursivelock.md)
- [IORegistryEntryApplierFunction](ioregistryentryapplierfunction.md)
- [IORegistryPlaneName](ioregistryplanename.md)
- [IOReportCategories](ioreportcategories.md)
- [IOReportConfigureAction](ioreportconfigureaction.md)
- [IOReportFormat](ioreportformat.md)
- [IOReportQuantity](ioreportquantity.md)
- [IOReportScaleFactor](ioreportscalefactor.md)
- [IOReportUnit](ioreportunit.md)
- [IOReportUnits](ioreportunits.md)
- [IOReportUpdateAction](ioreportupdateaction.md)
- [IOReturn](ioreturn.md)
- [IOSelect](ioselect.md)
- [IOService](ioservice-5h.md)
- [IOServiceApplierFunction](ioserviceapplierfunction.md)
- [IOServiceInterestContent64](ioserviceinterestcontent64.md)
- [IOServiceInterestHandler](ioserviceinteresthandler.md)
- [IOServiceInterestHandlerBlock](ioserviceinteresthandlerblock.md)
- [IOServiceMatchingNotificationHandler](ioservicematchingnotificationhandler.md)
- [IOServiceMatchingNotificationHandlerBlock](ioservicematchingnotificationhandlerblock.md)
- [IOServiceName](ioservicename.md)
- [IOServiceNotificationBlock](ioservicenotificationblock.md)
- [IOServiceNotificationHandler](ioservicenotificationhandler.md)
- [IOSimpleLock](iosimplelock.md)
- [IOStorageAccess](iostorageaccess.md)
- [IOStorageAttributes](iostorageattributes.md)
- [IOStorageCompletion](iostoragecompletion.md)
- [IOStorageCompletionAction](iostoragecompletionaction.md)
- [IOStorageExtent](iostorageextent.md)
- [IOStorageGetProvisionStatusOptions](iostoragegetprovisionstatusoptions.md)
- [IOStorageOptions](iostorageoptions.md)
- [IOStoragePriority](iostoragepriority.md)
- [IOStorageProvisionExtent](iostorageprovisionextent.md)
- [IOStorageSynchronizeOptions](iostoragesynchronizeoptions.md)
- [IOStorageUnmapOptions](iostorageunmapoptions.md)
- [IOStreamMode](iostreammode.md)
- [IOThread](iothread.md)
- [IOThreadFunc](iothreadfunc.md)
- [IOTimeStampIntervalConstantFiltered](iotimestampintervalconstantfiltered.md)
- [IOTimingInformation](iotiminginformation.md)
- [IOTrackingCallSiteInfo](iotrackingcallsiteinfo.md)
- [IOTrap](iotrap.md)
- [IOUserClientAsyncArgumentsArray](iouserclientasyncargumentsarray.md)
- [IOUserClientAsyncReferenceArray](iouserclientasyncreferencearray.md)
- [IOUserClientMethodArguments](iouserclientmethodarguments.md)
- [IOUserClientMethodDispatch](iouserclientmethoddispatch.md)
- [IOUserClientMethodFunction](iouserclientmethodfunction.md)
- [IOUserClientScalarArray](iouserclientscalararray.md)
- [IOVersion](ioversion.md)
- [IOVideoDeviceNotification](iovideodevicenotification.md)
- [IOVideoDeviceNotificationMessage](iovideodevicenotificationmessage.md)
- [IOVideoStreamDescription](iovideostreamdescription.md)
- [IOVirtualAddress](iovirtualaddress.md)
- [IOVirtualRange](iovirtualrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodetailedtiminginformationv2)*