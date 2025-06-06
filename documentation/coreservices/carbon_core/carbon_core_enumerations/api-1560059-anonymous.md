# Anonymous

**Framework**: Core Services

## Topics

### Constants
- [var errAEAccessorNotFound: Int](erraeaccessornotfound.md)
  There is no object accessor function forthe specified object class and container type
- [var errAEBadListItem: Int](erraebadlistitem.md)
  Operation involving a list item failed
- [var errAEBadTestKey: Int](erraebadtestkey.md)
  The descriptor in a test key is neithera comparison descriptor nor a logical descriptor
- [var errAEBufferTooSmall: Int](erraebuffertoosmall.md)
  Buffer for `AEFlattenDesc` toosmall
- [var errAEBuildSyntaxError: Int](erraebuildsyntaxerror.md)
  `AEBuildDesc` andrelated functions detected a syntax error
- [var errAECoercionFail: Int](erraecoercionfail.md)
  Data could not be coerced to the requesteddescriptor type
- [var errAECorruptData: Int](erraecorruptdata.md)
  Data in an Apple event could not be read
- [var errAEDescIsNull: Int](erraedescisnull.md)
  Attempt to perform an invalid operationon a null descriptor
- [var errAEDescNotFound: Int](erraedescnotfound.md)
  Descriptor was not found
- [var errAEDuplicateHandler: Int](erraeduplicatehandler.md)
  Attempt to install handler in table foridentical class and ID (1.1 or greater)
- [var errAEEmptyListContainer: Int](erraeemptylistcontainer.md)
  The container for an Apple event objectis specified by an empty list
- [var errAEEventFiltered: Int](erraeeventfiltered.md)
  Event has been filtered and should not bepropagated (1.1 or greater)
- [var errAEEventNotHandled: Int](erraeeventnothandled.md)
  Event wasn’t handled by an Apple eventhandler
- [var errAEHandlerNotFound: Int](erraehandlernotfound.md)
  No handler found for an Apple event
- [var errAEIllegalIndex: Int](erraeillegalindex.md)
  Not a valid list index
- [var errAEImpossibleRange: Int](erraeimpossiblerange.md)
  The range is not valid because it is impossiblefor a range to include the first and last objects that were specified;an example is a range in which the offset of the first object is greaterthan the offset of the last object
- [var errAENegativeCount: Int](erraenegativecount.md)
  An object-counting function returned a negativeresult
- [var errAENewerVersion: Int](erraenewerversion.md)
  Need a newer version of the Apple EventManager
- [var errAENoSuchLogical: Int](erraenosuchlogical.md)
  The logical operator in a logical descriptoris not `kAEAND`, `kAEOR`,or `kAENOT`
- [var errAENoSuchObject: Int](erraenosuchobject.md)
  Runtime resolution of an object failed.
- [var errAENoUserInteraction: Int](erraenouserinteraction.md)
  No user interaction allowed
- [var errAENotAEDesc: Int](erraenotaedesc.md)
  Not a valid descriptor
- [var errAENotASpecialFunction: Int](erraenotaspecialfunction.md)
  Wrong keyword for a special function
- [var errAENotAnObjSpec: Int](erraenotanobjspec.md)
- [var errAENotAppleEvent: Int](erraenotappleevent.md)
  The event is not in AppleEvent format.
- [var errAEParamMissed: Int](erraeparammissed.md)
  A required parameter was not accessed.
- [var errAEReceiveEscapeCurrent: Int](erraereceiveescapecurrent.md)
  Break out of lowest level only of `AEReceive` (1.1or greater)
- [var errAEReceiveTerminate: Int](erraereceiveterminate.md)
  Break out of all levels of `AEReceive` tothe topmost (1.1 or greater)
- [var errAERecordingIsAlreadyOn: Int](erraerecordingisalreadyon.md)
  Recording is already on
- [var errAEReplyNotArrived: Int](erraereplynotarrived.md)
  Reply has not yet arrived
- [var errAEReplyNotValid: Int](erraereplynotvalid.md)
  `AEResetTimer` was passed an invalid reply
- [var errAEStreamAlreadyConverted: Int](erraestreamalreadyconverted.md)
  Attempt to convert a stream that has alreadybeen converted
- [var errAEStreamBadNesting: Int](erraestreambadnesting.md)
  Nesting violation while streaming
- [var errAETimeout: Int](erraetimeout.md)
  Apple event timed out
- [var errAEUnknownAddressType: Int](erraeunknownaddresstype.md)
  Unknown Apple event address type
- [var errAEUnknownObjectType: Int](erraeunknownobjecttype.md)
  The object type isn’t recognized
- [var errAEUnknownSendMode: Int](erraeunknownsendmode.md)
  Invalid sending mode was passed
- [var errAEWaitCanceled: Int](erraewaitcanceled.md)
  User canceled out of wait loop for replyor receipt
- [var errAEWrongDataType: Int](erraewrongdatatype.md)
  Wrong descriptor type
- [var errAEWrongNumberArgs: Int](erraewrongnumberargs.md)
  The number of operands provided for the `kAENOT` logicaloperator is not 1


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/carbon_core_enumerations/1560059-anonymous)*