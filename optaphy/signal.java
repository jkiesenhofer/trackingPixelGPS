/*-----------------------------------------------------------------------------
-------------------------------------------------------------------------------
                            |
         FM-Pool            |  Optaphy: Thermoelectric Logistics Management
          9173              |  www.optaphy.com
                            |
-------------------------------------------------------------------------------
   Copyright (C) 2024 Optaphy SE
-------------------------------------------------------------------------------
-----------------------------------------------------------------------------*/
public class SignalProcessor implements signal, lambdaPrediction {
    @Override
    public void patch() {
        System.out.println("Patching signal...");
    }

    @Override
    public void impedance() {
        System.out.println("Calculating impedance...");
    }

    public static void main(String[] args) {
        SignalProcessor processor = new SignalProcessor();
        processor.patch();      // Calls the patch method
        processor.impedance();  // Calls the impedance method
    }
}
