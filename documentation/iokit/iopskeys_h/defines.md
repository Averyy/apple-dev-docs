# Defines

**Framework**: IOKit  
**Role**: API Collection

## Topics

### Constants
- [kIOPSACPowerValue](../kiopsacpowervalue.md)
  Value for key kIOPSPowerSourceStateKey. Power source is connected to external or AC power, and is not draining the internal battery.
- [kIOPSBatteryFailureModesKey](../kiopsbatteryfailuremodeskey.md)
  Enumerates a battery's failures and error conditions.
- [kIOPSBatteryHealthConditionKey](../kiopsbatteryhealthconditionkey.md)
  kIOPSBatteryHealthConditionKey broadly describes the battery's health.
- [kIOPSBatteryHealthKey](../kiopsbatteryhealthkey.md)
  CFDictionary key for the current power source's "health" estimate.
- [kIOPSBatteryPowerValue](../kiopsbatterypowervalue.md)
  Value for key kIOPSPowerSourceStateKey. Power source is currently using the internal battery.
- [kIOPSCheckBatteryValue](../kiopscheckbatteryvalue.md)
  Value for key [`kIOPSBatteryHealthConditionKey`](../kiopsbatteryhealthconditionkey.md)
- [kIOPSCommandDelayedRemovePowerKey](../kiopscommanddelayedremovepowerkey.md)
  Command to give a UPS when it should remove power from its AC plugs in a specified amount of time
- [kIOPSCommandEnableAudibleAlarmKey](../kiopscommandenableaudiblealarmkey.md)
  Command to give a UPS when it should either enable or disable the audible alarm.
- [kIOPSCommandStartupDelayKey](../kiopscommandstartupdelaykey.md)
  Tell UPS how long it should wait for
- [kIOPSCurrentCapacityKey](../kiopscurrentcapacitykey.md)
  CFDictionary key for the current power source's capacity.
- [kIOPSCurrentKey](../kiopscurrentkey.md)
  CFDictionary key for the current power source's electrical current.
- [kIOPSDeadWarnLevelKey](../kiopsdeadwarnlevelkey.md)
  Key for the "Shutdown System" low power trigger-level. Default is 20%.
- [kIOPSDesignCapacityKey](../kiopsdesigncapacitykey.md)
  CFDictionary key for the current power source's design capacity
- [kIOPSDynamicStorePath](../kiopsdynamicstorepath.md)
  This is only used for internal bookkeeping, and should be ignored.
- [kIOPSFailureCellImbalance](../kiopsfailurecellimbalance.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailureChargeFET](../kiopsfailurechargefet.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailureChargeOverCurrent](../kiopsfailurechargeovercurrent.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailureChargeOverTemp](../kiopsfailurechargeovertemp.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailureDataFlushFault](../kiopsfailuredataflushfault.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailureDischargeFET](../kiopsfailuredischargefet.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailureDischargeOverCurrent](../kiopsfailuredischargeovercurrent.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailureDischargeOverTemp](../kiopsfailuredischargeovertemp.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailureExternalInput](../kiopsfailureexternalinput.md)
  Value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailureFuseBlown](../kiopsfailurefuseblown.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailureOpenThermistor](../kiopsfailureopenthermistor.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailurePeriodicAFEComms](../kiopsfailureperiodicafecomms.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailurePermanentAFEComms](../kiopsfailurepermanentafecomms.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFailureSafetyOverVoltage](../kiopsfailuresafetyovervoltage.md)
  Potential value for key [`kIOPSBatteryFailureModesKey`](../kiopsbatteryfailuremodeskey.md)
- [kIOPSFairValue](../kiopsfairvalue.md)
  Value for key [`kIOPSBatteryHealthKey`](../kiopsbatteryhealthkey.md).
- [kIOPSGoodValue](../kiopsgoodvalue.md)
  Value for key [`kIOPSBatteryHealthKey`](../kiopsbatteryhealthkey.md).
- [kIOPSHardwareSerialNumberKey](../kiopshardwareserialnumberkey.md)
  A unique serial number that identifies the power source.
- [kIOPSHealthConfidenceKey](../kiopshealthconfidencekey.md)
  CFDictionary key for our confidence in the accuracy of our power source's "health" estimate.
- [kIOPSInternalBatteryType](../kiopsinternalbatterytype.md)
  Represents a battery residing inside a Mac.
- [kIOPSInternalType](../kiopsinternaltype.md)
  Value for key [`kIOPSTransportTypeKey`](../kiopstransporttypekey.md). Indicates the power source is an internal battery.
- [kIOPSIsChargedKey](../kiopsischargedkey.md)
  CFDictionary key indicates whether the battery is charged.
- [kIOPSIsChargingKey](../kiopsischargingkey.md)
  CFDictionary key for the current power source's charging state
- [kIOPSIsFinishingChargeKey](../kiopsisfinishingchargekey.md)
  CFDictionary key indicates whether the battery is finishing off its charge.
- [kIOPSIsPresentKey](../kiopsispresentkey.md)
  CFDictionary key for the current power source's presence.
- [kIOPSLowWarnLevelKey](../kiopslowwarnlevelkey.md)
  Key for the "Warning" UPS low power trigger-level. Default is 50%.
- [kIOPSMaxCapacityKey](../kiopsmaxcapacitykey.md)
  CFDictionary key for the current power source's maximum or "Full Charge Capacity"
- [kIOPSMaxErrKey](../kiopsmaxerrkey.md)
  CFDictionary key for the current power source's percentage error in capacity reporting.
- [kIOPSNameKey](../kiopsnamekey.md)
  CFDictionary key for the current power source's name.
- [kIOPSNetworkTransportType](../kiopsnetworktransporttype.md)
  Value for key [`kIOPSTransportTypeKey`](../kiopstransporttypekey.md).
- [kIOPSOffLineValue](../kiopsofflinevalue.md)
  Value for key kIOPSPowerSourceStateKey. Power source is off-line or no longer connected.
- [kIOPSPermanentFailureValue](../kiopspermanentfailurevalue.md)
  Value for key [`kIOPSBatteryHealthConditionKey`](../kiopsbatteryhealthconditionkey.md)
- [kIOPSPoorValue](../kiopspoorvalue.md)
  Value for key [`kIOPSBatteryHealthKey`](../kiopsbatteryhealthkey.md).
- [kIOPSPowerAdapterCurrentKey](../kiopspoweradaptercurrentkey.md)
  This key refers to the current of the external AC power adapter attached to a portable. The value associated with this key is a CFNumberRef kCFNumberIntType integer value, in units of mAmps.
- [kIOPSPowerAdapterFamilyKey](../kiopspoweradapterfamilykey.md)
  The power adapter's family code. The value associated with this key is a CFNumberRef kCFNumberIntType integer value
- [kIOPSPowerAdapterIDKey](../kiopspoweradapteridkey.md)
  This key refers to the attached external AC power adapter's ID. The value associated with this key is a CFNumberRef kCFNumberIntType integer.
- [kIOPSPowerAdapterRevisionKey](../kiopspoweradapterrevisionkey.md)
  The power adapter's revision. The value associated with this key is a CFNumberRef kCFNumberIntType integer value
- [kIOPSPowerAdapterSerialNumberKey](../kiopspoweradapterserialnumberkey.md)
  The power adapter's serial number. The value associated with this key is a CFNumberRef kCFNumberIntType integer value
- [kIOPSPowerAdapterSourceKey](../kiopspoweradaptersourcekey.md)
  This key refers to the source of the power. The value associated with this key is a CFNumberRef kCFNumberIntType integer value.
- [kIOPSPowerAdapterWattsKey](../kiopspoweradapterwattskey.md)
  This key refers to the wattage of the external AC power adapter attached to a portable. The value associated with this key is a CFNumberRef kCFNumberIntType integer value, in units of watts.
- [kIOPSPowerSourceIDKey](../kiopspowersourceidkey.md)
  CFNumber key uniquely identifying a UPS attached to the system.
- [kIOPSPowerSourceStateKey](../kiopspowersourcestatekey.md)
  CFDictionary key for the current source of power.
- [kIOPSSerialTransportType](../kiopsserialtransporttype.md)
  Value for key [`kIOPSTransportTypeKey`](../kiopstransporttypekey.md).
- [kIOPSTimeToEmptyKey](../kiopstimetoemptykey.md)
  CFDictionary key for the current power source's time remaining until empty.
- [kIOPSTimeToFullChargeKey](../kiopstimetofullchargekey.md)
  CFDictionary key for the current power source's time remaining until empty.
- [kIOPSTransportTypeKey](../kiopstransporttypekey.md)
  CFDictionary key for the current power source's data transport type (e.g. the means that the power source conveys power source data to the macOS machine).
- [kIOPSTypeKey](../kiopstypekey.md)
  CFDictionary key for the type of the power source
- [kIOPSUPSManagementClaimed](../kiopsupsmanagementclaimed.md)
  Claims UPS management for a third-party driver.
- [kIOPSUPSType](../kiopsupstype.md)
  Represents an external attached UPS.
- [kIOPSUSBTransportType](../kiopsusbtransporttype.md)
  Value for key [`kIOPSTransportTypeKey`](../kiopstransporttypekey.md).
- [kIOPSVendorDataKey](../kiopsvendordatakey.md)
  CFDictionary key for arbitrary vendor data.
- [kIOPSVoltageKey](../kiopsvoltagekey.md)
  CFDictionary key for the current power source's electrical voltage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopskeys_h/defines)*