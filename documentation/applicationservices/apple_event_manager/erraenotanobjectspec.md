# errAENotAnObjectSpec

**Framework**: Application Services  
**Kind**: econst

The `objSpecifier` parameterof `AEResolve` is not anobject specifier

## See Also

### Result Codes
- [noPortErr](../../coreservices/api-1560074-anonymous/noporterr.md)
  Client hasn’t set `'SIZE'` resource toindicate awareness of high-level events
- [destPortErr](../../coreservices/api-1560074-anonymous/destporterr.md)
  Server hasn’t set `'SIZE'` resource toindicate awareness of high-level events, or else is not present
- [sessClosedErr](../../coreservices/api-1560074-anonymous/sessclosederr.md)
  The `kAEDontReconnect` flagin the `sendMode` parameterwas set and the server quit, then restarted
- [errAECoercionFail](../../coreservices/api-1560059-anonymous/erraecoercionfail.md)
  Data could not be coerced to the requesteddescriptor type
- [errAEDescNotFound](../../coreservices/api-1560059-anonymous/erraedescnotfound.md)
  Descriptor was not found
- [errAECorruptData](../../coreservices/api-1560059-anonymous/erraecorruptdata.md)
  Data in an Apple event could not be read
- [errAEWrongDataType](../../coreservices/api-1560059-anonymous/erraewrongdatatype.md)
  Wrong descriptor type
- [errAENotAEDesc](../../coreservices/api-1560059-anonymous/erraenotaedesc.md)
  Not a valid descriptor
- [errAEBadListItem](../../coreservices/api-1560059-anonymous/erraebadlistitem.md)
  Operation involving a list item failed
- [errAENewerVersion](../../coreservices/api-1560059-anonymous/erraenewerversion.md)
  Need a newer version of the Apple EventManager
- [errAENotAppleEvent](../../coreservices/api-1560059-anonymous/erraenotappleevent.md)
  The event is not in AppleEvent format.
- [errAEEventNotHandled](../../coreservices/api-1560059-anonymous/erraeeventnothandled.md)
  Event wasn’t handled by an Apple eventhandler
- [errAEReplyNotValid](../../coreservices/api-1560059-anonymous/erraereplynotvalid.md)
  `AEResetTimer` was passed an invalid reply
- [errAEUnknownSendMode](../../coreservices/api-1560059-anonymous/erraeunknownsendmode.md)
  Invalid sending mode was passed
- [errAEWaitCanceled](../../coreservices/api-1560059-anonymous/erraewaitcanceled.md)
  User canceled out of wait loop for replyor receipt
- [errAETimeout](../../coreservices/api-1560059-anonymous/erraetimeout.md)
  Apple event timed out
- [errAENoUserInteraction](../../coreservices/api-1560059-anonymous/erraenouserinteraction.md)
  No user interaction allowed
- [errAENotASpecialFunction](../../coreservices/api-1560059-anonymous/erraenotaspecialfunction.md)
  Wrong keyword for a special function
- [errAEParamMissed](../../coreservices/api-1560059-anonymous/erraeparammissed.md)
  A required parameter was not accessed.
- [errAEUnknownAddressType](../../coreservices/api-1560059-anonymous/erraeunknownaddresstype.md)
  Unknown Apple event address type
- [errAEHandlerNotFound](../../coreservices/api-1560059-anonymous/erraehandlernotfound.md)
  No handler found for an Apple event
- [errAEReplyNotArrived](../../coreservices/api-1560059-anonymous/erraereplynotarrived.md)
  Reply has not yet arrived
- [errAEIllegalIndex](../../coreservices/api-1560059-anonymous/erraeillegalindex.md)
  Not a valid list index
- [errAEImpossibleRange](../../coreservices/api-1560059-anonymous/erraeimpossiblerange.md)
  The range is not valid because it is impossiblefor a range to include the first and last objects that were specified;an example is a range in which the offset of the first object is greaterthan the offset of the last object
- [errAEWrongNumberArgs](../../coreservices/api-1560059-anonymous/erraewrongnumberargs.md)
  The number of operands provided for the `kAENOT` logicaloperator is not 1
- [errAEAccessorNotFound](../../coreservices/api-1560059-anonymous/erraeaccessornotfound.md)
  There is no object accessor function forthe specified object class and container type
- [errAENoSuchLogical](../../coreservices/api-1560059-anonymous/erraenosuchlogical.md)
  The logical operator in a logical descriptoris not `kAEAND`, `kAEOR`,or `kAENOT`
- [errAEBadTestKey](../../coreservices/api-1560059-anonymous/erraebadtestkey.md)
  The descriptor in a test key is neithera comparison descriptor nor a logical descriptor
- [errAENoSuchObject](../../coreservices/api-1560059-anonymous/erraenosuchobject.md)
  Runtime resolution of an object failed.
- [errAENegativeCount](../../coreservices/api-1560059-anonymous/erraenegativecount.md)
  An object-counting function returned a negativeresult
- [errAEEmptyListContainer](../../coreservices/api-1560059-anonymous/erraeemptylistcontainer.md)
  The container for an Apple event objectis specified by an empty list
- [errAEUnknownObjectType](../../coreservices/api-1560059-anonymous/erraeunknownobjecttype.md)
  The object type isn’t recognized
- [errAERecordingIsAlreadyOn](../../coreservices/api-1560059-anonymous/erraerecordingisalreadyon.md)
  Recording is already on
- [errAEReceiveTerminate](../../coreservices/api-1560059-anonymous/erraereceiveterminate.md)
  Break out of all levels of `AEReceive` tothe topmost (1.1 or greater)
- [errAEReceiveEscapeCurrent](../../coreservices/api-1560059-anonymous/erraereceiveescapecurrent.md)
  Break out of lowest level only of `AEReceive` (1.1or greater)
- [errAEEventFiltered](../../coreservices/api-1560059-anonymous/erraeeventfiltered.md)
  Event has been filtered and should not bepropagated (1.1 or greater)
- [errAEDuplicateHandler](../../coreservices/api-1560059-anonymous/erraeduplicatehandler.md)
  Attempt to install handler in table foridentical class and ID (1.1 or greater)
- [errAEStreamBadNesting](../../coreservices/api-1560059-anonymous/erraestreambadnesting.md)
  Nesting violation while streaming
- [errAEStreamAlreadyConverted](../../coreservices/api-1560059-anonymous/erraestreamalreadyconverted.md)
  Attempt to convert a stream that has alreadybeen converted
- [errAEDescIsNull](../../coreservices/api-1560059-anonymous/erraedescisnull.md)
  Attempt to perform an invalid operationon a null descriptor
- [errAEBuildSyntaxError](../../coreservices/api-1560059-anonymous/erraebuildsyntaxerror.md)
  `AEBuildDesc` andrelated functions detected a syntax error
- [errAEBufferTooSmall](../../coreservices/api-1560059-anonymous/erraebuffertoosmall.md)
  Buffer for `AEFlattenDesc` toosmall
- [errASCantConsiderAndIgnore](../../coreservices/api-1559945-anonymous/errascantconsiderandignore.md)
  Can’t both consider and ignore <attribute>.
- [errASCantCompareMoreThan32k](../../coreservices/api-1559945-anonymous/errascantcomparemorethan32k.md)
  Can’t perform operation on text longerthan 32K bytes.
- [errASTerminologyNestingTooDeep](../../coreservices/api-1559945-anonymous/errasterminologynestingtoodeep.md)
  Tell statements are nested too deeply.
- [errASIllegalFormalParameter](../../coreservices/api-1559945-anonymous/errasillegalformalparameter.md)
  <name> is illegal as a formal parameter.
- [errASParameterNotForEvent](../../coreservices/api-1559945-anonymous/errasparameternotforevent.md)
  <name> is not a parameter name for the event <event>.
- [errASNoResultReturned](../../coreservices/api-1559945-anonymous/errasnoresultreturned.md)
  No result was returned for some argumentof this expression. 
- [errAEEventFailed](../../coreservices/api-1560036-anonymous/erraeeventfailed.md)
  Apple event handler failed.
- [errAETypeError](../../coreservices/api-1560036-anonymous/erraetypeerror.md)
  A descriptor type mismatch occurred.
- [errAEBadKeyForm](../../coreservices/api-1560036-anonymous/erraebadkeyform.md)
  Invalid key form.
- [errAENotModifiable](../../coreservices/api-1560036-anonymous/erraenotmodifiable.md)
  Can't set <object or data> to <object or data>. Access not allowed.
- [errAEPrivilegeError](../../coreservices/api-1560036-anonymous/erraeprivilegeerror.md)
  A privilege violation occurred.
- [errAEReadDenied](../../coreservices/api-1560036-anonymous/erraereaddenied.md)
  The read operation was not allowed.
- [errAEWriteDenied](../../coreservices/api-1560036-anonymous/erraewritedenied.md)
  Can't set <object or data> to <object or data>. 
- [errAEIndexTooLarge](../../coreservices/api-1560036-anonymous/erraeindextoolarge.md)
  The index of the event is too large to bevalid.
- [errAENotAnElement](../../coreservices/api-1560036-anonymous/erraenotanelement.md)
  The specified object is a property, notan element.
- [errAECantSupplyType](../../coreservices/api-1560036-anonymous/erraecantsupplytype.md)
  Can’t supply the requested descriptortype for the data.
- [errAECantHandleClass](../../coreservices/api-1560036-anonymous/erraecanthandleclass.md)
  The Apple event handler can’t handle objectsof this class.
- [errAEInTransaction](../../coreservices/api-1560036-anonymous/erraeintransaction.md)
  Couldn’t handle this command because itwasn’t part of the current transaction.
- [errAENoSuchTransaction](../../coreservices/api-1560036-anonymous/erraenosuchtransaction.md)
  The transaction to which this command belongedisn’t a valid transaction.
- [errAENoUserSelection](../../coreservices/api-1560036-anonymous/erraenouserselection.md)
  There is no user selection.
- [errAENotASingleObject](../../coreservices/api-1560036-anonymous/erraenotasingleobject.md)
  Handler only handles single objects.
- [errAECantUndo](../../coreservices/api-1560036-anonymous/erraecantundo.md)
  Can’t undo the previous Apple event oruser action.
- [errAENotAnEnumMember](../../coreservices/api-1560036-anonymous/erraenotanenummember.md)
  Enumerated value in `SetData` is notallowed for this property
- [errAECantPutThatThere](../../coreservices/api-1560036-anonymous/erraecantputthatthere.md)
  In make new, duplicate, etc. class can'tbe an element of container
- [errAEPropertiesClash](../../coreservices/api-1560036-anonymous/erraepropertiesclash.md)
  Illegal combination of properties settingsfor SetData, make new, or duplicate


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager/erraenotanobjectspec)*