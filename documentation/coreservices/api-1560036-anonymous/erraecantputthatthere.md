# errAECantPutThatThere

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

In make new, duplicate, etc. class can'tbe an element of container

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
errAECantPutThatThere = -10024
```

## See Also

### Result Codes
- [noPortErr](../api-1560074-anonymous/noporterr.md)
  Client hasn’t set `'SIZE'` resource toindicate awareness of high-level events
- [destPortErr](../api-1560074-anonymous/destporterr.md)
  Server hasn’t set `'SIZE'` resource toindicate awareness of high-level events, or else is not present
- [sessClosedErr](../api-1560074-anonymous/sessclosederr.md)
  The `kAEDontReconnect` flagin the `sendMode` parameterwas set and the server quit, then restarted
- [errAECoercionFail](../api-1560059-anonymous/erraecoercionfail.md)
  Data could not be coerced to the requesteddescriptor type
- [errAEDescNotFound](../api-1560059-anonymous/erraedescnotfound.md)
  Descriptor was not found
- [errAECorruptData](../api-1560059-anonymous/erraecorruptdata.md)
  Data in an Apple event could not be read
- [errAEWrongDataType](../api-1560059-anonymous/erraewrongdatatype.md)
  Wrong descriptor type
- [errAENotAEDesc](../api-1560059-anonymous/erraenotaedesc.md)
  Not a valid descriptor
- [errAEBadListItem](../api-1560059-anonymous/erraebadlistitem.md)
  Operation involving a list item failed
- [errAENewerVersion](../api-1560059-anonymous/erraenewerversion.md)
  Need a newer version of the Apple EventManager
- [errAENotAppleEvent](../api-1560059-anonymous/erraenotappleevent.md)
  The event is not in AppleEvent format.
- [errAEEventNotHandled](../api-1560059-anonymous/erraeeventnothandled.md)
  Event wasn’t handled by an Apple eventhandler
- [errAEReplyNotValid](../api-1560059-anonymous/erraereplynotvalid.md)
  `AEResetTimer` was passed an invalid reply
- [errAEUnknownSendMode](../api-1560059-anonymous/erraeunknownsendmode.md)
  Invalid sending mode was passed
- [errAEWaitCanceled](../api-1560059-anonymous/erraewaitcanceled.md)
  User canceled out of wait loop for replyor receipt
- [errAETimeout](../api-1560059-anonymous/erraetimeout.md)
  Apple event timed out
- [errAENoUserInteraction](../api-1560059-anonymous/erraenouserinteraction.md)
  No user interaction allowed
- [errAENotASpecialFunction](../api-1560059-anonymous/erraenotaspecialfunction.md)
  Wrong keyword for a special function
- [errAEParamMissed](../api-1560059-anonymous/erraeparammissed.md)
  A required parameter was not accessed.
- [errAEUnknownAddressType](../api-1560059-anonymous/erraeunknownaddresstype.md)
  Unknown Apple event address type
- [errAEHandlerNotFound](../api-1560059-anonymous/erraehandlernotfound.md)
  No handler found for an Apple event
- [errAEReplyNotArrived](../api-1560059-anonymous/erraereplynotarrived.md)
  Reply has not yet arrived
- [errAEIllegalIndex](../api-1560059-anonymous/erraeillegalindex.md)
  Not a valid list index
- [errAEImpossibleRange](../api-1560059-anonymous/erraeimpossiblerange.md)
  The range is not valid because it is impossiblefor a range to include the first and last objects that were specified;an example is a range in which the offset of the first object is greaterthan the offset of the last object
- [errAEWrongNumberArgs](../api-1560059-anonymous/erraewrongnumberargs.md)
  The number of operands provided for the `kAENOT` logicaloperator is not 1
- [errAEAccessorNotFound](../api-1560059-anonymous/erraeaccessornotfound.md)
  There is no object accessor function forthe specified object class and container type
- [errAENoSuchLogical](../api-1560059-anonymous/erraenosuchlogical.md)
  The logical operator in a logical descriptoris not `kAEAND`, `kAEOR`,or `kAENOT`
- [errAEBadTestKey](../api-1560059-anonymous/erraebadtestkey.md)
  The descriptor in a test key is neithera comparison descriptor nor a logical descriptor
- [errAENotAnObjectSpec](../../applicationservices/apple_event_manager/erraenotanobjectspec.md)
  The `objSpecifier` parameterof `AEResolve` is not anobject specifier
- [errAENoSuchObject](../api-1560059-anonymous/erraenosuchobject.md)
  Runtime resolution of an object failed.
- [errAENegativeCount](../api-1560059-anonymous/erraenegativecount.md)
  An object-counting function returned a negativeresult
- [errAEEmptyListContainer](../api-1560059-anonymous/erraeemptylistcontainer.md)
  The container for an Apple event objectis specified by an empty list
- [errAEUnknownObjectType](../api-1560059-anonymous/erraeunknownobjecttype.md)
  The object type isn’t recognized
- [errAERecordingIsAlreadyOn](../api-1560059-anonymous/erraerecordingisalreadyon.md)
  Recording is already on
- [errAEReceiveTerminate](../api-1560059-anonymous/erraereceiveterminate.md)
  Break out of all levels of `AEReceive` tothe topmost (1.1 or greater)
- [errAEReceiveEscapeCurrent](../api-1560059-anonymous/erraereceiveescapecurrent.md)
  Break out of lowest level only of `AEReceive` (1.1or greater)
- [errAEEventFiltered](../api-1560059-anonymous/erraeeventfiltered.md)
  Event has been filtered and should not bepropagated (1.1 or greater)
- [errAEDuplicateHandler](../api-1560059-anonymous/erraeduplicatehandler.md)
  Attempt to install handler in table foridentical class and ID (1.1 or greater)
- [errAEStreamBadNesting](../api-1560059-anonymous/erraestreambadnesting.md)
  Nesting violation while streaming
- [errAEStreamAlreadyConverted](../api-1560059-anonymous/erraestreamalreadyconverted.md)
  Attempt to convert a stream that has alreadybeen converted
- [errAEDescIsNull](../api-1560059-anonymous/erraedescisnull.md)
  Attempt to perform an invalid operationon a null descriptor
- [errAEBuildSyntaxError](../api-1560059-anonymous/erraebuildsyntaxerror.md)
  `AEBuildDesc` andrelated functions detected a syntax error
- [errAEBufferTooSmall](../api-1560059-anonymous/erraebuffertoosmall.md)
  Buffer for `AEFlattenDesc` toosmall
- [errASCantConsiderAndIgnore](../api-1559945-anonymous/errascantconsiderandignore.md)
  Can’t both consider and ignore <attribute>.
- [errASCantCompareMoreThan32k](../api-1559945-anonymous/errascantcomparemorethan32k.md)
  Can’t perform operation on text longerthan 32K bytes.
- [errASTerminologyNestingTooDeep](../api-1559945-anonymous/errasterminologynestingtoodeep.md)
  Tell statements are nested too deeply.
- [errASIllegalFormalParameter](../api-1559945-anonymous/errasillegalformalparameter.md)
  <name> is illegal as a formal parameter.
- [errASParameterNotForEvent](../api-1559945-anonymous/errasparameternotforevent.md)
  <name> is not a parameter name for the event <event>.
- [errASNoResultReturned](../api-1559945-anonymous/errasnoresultreturned.md)
  No result was returned for some argumentof this expression. 
- [errAEEventFailed](./erraeeventfailed.md)
  Apple event handler failed.
- [errAETypeError](./erraetypeerror.md)
  A descriptor type mismatch occurred.
- [errAEBadKeyForm](./erraebadkeyform.md)
  Invalid key form.
- [errAENotModifiable](./erraenotmodifiable.md)
  Can't set <object or data> to <object or data>. Access not allowed.
- [errAEPrivilegeError](./erraeprivilegeerror.md)
  A privilege violation occurred.
- [errAEReadDenied](./erraereaddenied.md)
  The read operation was not allowed.
- [errAEWriteDenied](./erraewritedenied.md)
  Can't set <object or data> to <object or data>. 
- [errAEIndexTooLarge](./erraeindextoolarge.md)
  The index of the event is too large to bevalid.
- [errAENotAnElement](./erraenotanelement.md)
  The specified object is a property, notan element.
- [errAECantSupplyType](./erraecantsupplytype.md)
  Can’t supply the requested descriptortype for the data.
- [errAECantHandleClass](./erraecanthandleclass.md)
  The Apple event handler can’t handle objectsof this class.
- [errAEInTransaction](./erraeintransaction.md)
  Couldn’t handle this command because itwasn’t part of the current transaction.
- [errAENoSuchTransaction](./erraenosuchtransaction.md)
  The transaction to which this command belongedisn’t a valid transaction.
- [errAENoUserSelection](./erraenouserselection.md)
  There is no user selection.
- [errAENotASingleObject](./erraenotasingleobject.md)
  Handler only handles single objects.
- [errAECantUndo](./erraecantundo.md)
  Can’t undo the previous Apple event oruser action.
- [errAENotAnEnumMember](./erraenotanenummember.md)
  Enumerated value in `SetData` is notallowed for this property
- [errAEPropertiesClash](./erraepropertiesclash.md)
  Illegal combination of properties settingsfor SetData, make new, or duplicate


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1560036-anonymous/erraecantputthatthere)*