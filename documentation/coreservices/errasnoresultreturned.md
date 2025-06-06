# errASNoResultReturned

**Framework**: Core Services  
**Kind**: data

No result was returned for some argumentof this expression. 

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var errASNoResultReturned: Int { get }
```

## See Also

- [var noPortErr: Int](noporterr.md)
  Client hasn’t set `'SIZE'` resource toindicate awareness of high-level events
- [var destPortErr: Int](destporterr.md)
  Server hasn’t set `'SIZE'` resource toindicate awareness of high-level events, or else is not present
- [var sessClosedErr: Int](sessclosederr.md)
  The `kAEDontReconnect` flagin the `sendMode` parameterwas set and the server quit, then restarted
- [var errAECoercionFail: Int](erraecoercionfail.md)
  Data could not be coerced to the requesteddescriptor type
- [var errAEDescNotFound: Int](erraedescnotfound.md)
  Descriptor was not found
- [var errAECorruptData: Int](erraecorruptdata.md)
  Data in an Apple event could not be read
- [var errAEWrongDataType: Int](erraewrongdatatype.md)
  Wrong descriptor type
- [var errAENotAEDesc: Int](erraenotaedesc.md)
  Not a valid descriptor
- [var errAEBadListItem: Int](erraebadlistitem.md)
  Operation involving a list item failed
- [var errAENewerVersion: Int](erraenewerversion.md)
  Need a newer version of the Apple EventManager
- [var errAENotAppleEvent: Int](erraenotappleevent.md)
  The event is not in AppleEvent format.
- [var errAEEventNotHandled: Int](erraeeventnothandled.md)
  Event wasn’t handled by an Apple eventhandler
- [var errAEReplyNotValid: Int](erraereplynotvalid.md)
  `AEResetTimer` was passed an invalid reply
- [var errAEUnknownSendMode: Int](erraeunknownsendmode.md)
  Invalid sending mode was passed
- [var errAEWaitCanceled: Int](erraewaitcanceled.md)
  User canceled out of wait loop for replyor receipt
- [var errAETimeout: Int](erraetimeout.md)
  Apple event timed out
- [var errAENoUserInteraction: Int](erraenouserinteraction.md)
  No user interaction allowed
- [var errAENotASpecialFunction: Int](erraenotaspecialfunction.md)
  Wrong keyword for a special function
- [var errAEParamMissed: Int](erraeparammissed.md)
  A required parameter was not accessed.
- [var errAEUnknownAddressType: Int](erraeunknownaddresstype.md)
  Unknown Apple event address type
- [var errAEHandlerNotFound: Int](erraehandlernotfound.md)
  No handler found for an Apple event
- [var errAEReplyNotArrived: Int](erraereplynotarrived.md)
  Reply has not yet arrived
- [var errAEIllegalIndex: Int](erraeillegalindex.md)
  Not a valid list index
- [var errAEImpossibleRange: Int](erraeimpossiblerange.md)
  The range is not valid because it is impossiblefor a range to include the first and last objects that were specified;an example is a range in which the offset of the first object is greaterthan the offset of the last object
- [var errAEWrongNumberArgs: Int](erraewrongnumberargs.md)
  The number of operands provided for the `kAENOT` logicaloperator is not 1
- [var errAEAccessorNotFound: Int](erraeaccessornotfound.md)
  There is no object accessor function forthe specified object class and container type
- [var errAENoSuchLogical: Int](erraenosuchlogical.md)
  The logical operator in a logical descriptoris not `kAEAND`, `kAEOR`,or `kAENOT`
- [var errAEBadTestKey: Int](erraebadtestkey.md)
  The descriptor in a test key is neithera comparison descriptor nor a logical descriptor
- [var errAENoSuchObject: Int](erraenosuchobject.md)
  Runtime resolution of an object failed.
- [var errAENegativeCount: Int](erraenegativecount.md)
  An object-counting function returned a negativeresult
- [var errAEEmptyListContainer: Int](erraeemptylistcontainer.md)
  The container for an Apple event objectis specified by an empty list
- [var errAEUnknownObjectType: Int](erraeunknownobjecttype.md)
  The object type isn’t recognized
- [var errAERecordingIsAlreadyOn: Int](erraerecordingisalreadyon.md)
  Recording is already on
- [var errAEReceiveTerminate: Int](erraereceiveterminate.md)
  Break out of all levels of `AEReceive` tothe topmost (1.1 or greater)
- [var errAEReceiveEscapeCurrent: Int](erraereceiveescapecurrent.md)
  Break out of lowest level only of `AEReceive` (1.1or greater)
- [var errAEEventFiltered: Int](erraeeventfiltered.md)
  Event has been filtered and should not bepropagated (1.1 or greater)
- [var errAEDuplicateHandler: Int](erraeduplicatehandler.md)
  Attempt to install handler in table foridentical class and ID (1.1 or greater)
- [var errAEStreamBadNesting: Int](erraestreambadnesting.md)
  Nesting violation while streaming
- [var errAEStreamAlreadyConverted: Int](erraestreamalreadyconverted.md)
  Attempt to convert a stream that has alreadybeen converted
- [var errAEDescIsNull: Int](erraedescisnull.md)
  Attempt to perform an invalid operationon a null descriptor
- [var errAEBuildSyntaxError: Int](erraebuildsyntaxerror.md)
  `AEBuildDesc` andrelated functions detected a syntax error
- [var errAEBufferTooSmall: Int](erraebuffertoosmall.md)
  Buffer for `AEFlattenDesc` toosmall
- [var errASCantConsiderAndIgnore: Int](errascantconsiderandignore.md)
  Can’t both consider and ignore <attribute>.
- [var errASCantCompareMoreThan32k: Int](errascantcomparemorethan32k.md)
  Can’t perform operation on text longerthan 32K bytes.
- [var errASTerminologyNestingTooDeep: Int](errasterminologynestingtoodeep.md)
  Tell statements are nested too deeply.
- [var errASIllegalFormalParameter: Int](errasillegalformalparameter.md)
  <name> is illegal as a formal parameter.
- [var errASParameterNotForEvent: Int](errasparameternotforevent.md)
  <name> is not a parameter name for the event <event>.
- [var errAEEventFailed: Int](erraeeventfailed.md)
  Apple event handler failed.
- [var errAETypeError: Int](erraetypeerror.md)
  A descriptor type mismatch occurred.
- [var errAEBadKeyForm: Int](erraebadkeyform.md)
  Invalid key form.
- [var errAENotModifiable: Int](erraenotmodifiable.md)
  Can't set <object or data> to <object or data>. Access not allowed.
- [var errAEPrivilegeError: Int](erraeprivilegeerror.md)
  A privilege violation occurred.
- [var errAEReadDenied: Int](erraereaddenied.md)
  The read operation was not allowed.
- [var errAEWriteDenied: Int](erraewritedenied.md)
  Can't set <object or data> to <object or data>. 
- [var errAEIndexTooLarge: Int](erraeindextoolarge.md)
  The index of the event is too large to bevalid.
- [var errAENotAnElement: Int](erraenotanelement.md)
  The specified object is a property, notan element.
- [var errAECantSupplyType: Int](erraecantsupplytype.md)
  Can’t supply the requested descriptortype for the data.
- [var errAECantHandleClass: Int](erraecanthandleclass.md)
  The Apple event handler can’t handle objectsof this class.
- [var errAEInTransaction: Int](erraeintransaction.md)
  Couldn’t handle this command because itwasn’t part of the current transaction.
- [var errAENoSuchTransaction: Int](erraenosuchtransaction.md)
  The transaction to which this command belongedisn’t a valid transaction.
- [var errAENoUserSelection: Int](erraenouserselection.md)
  There is no user selection.
- [var errAENotASingleObject: Int](erraenotasingleobject.md)
  Handler only handles single objects.
- [var errAECantUndo: Int](erraecantundo.md)
  Can’t undo the previous Apple event oruser action.
- [var errAENotAnEnumMember: Int](erraenotanenummember.md)
  Enumerated value in `SetData` is notallowed for this property
- [var errAECantPutThatThere: Int](erraecantputthatthere.md)
  In make new, duplicate, etc. class can'tbe an element of container
- [var errAEPropertiesClash: Int](erraepropertiesclash.md)
  Illegal combination of properties settingsfor SetData, make new, or duplicate


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/errasnoresultreturned)*