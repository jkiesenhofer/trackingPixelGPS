/*-----------------------------------------------------------------------------
-------------------------------------------------------------------------------
                            |
         FM-Pool            |  Fluidmotion: Thermoelectric Control Engineering
          9173              |  www.fluidmotion.nl
                            |
-------------------------------------------------------------------------------
   Copyright (C) 2024 Fluidmotion B.V.
-------------------------------------------------------------------------------
-----------------------------------------------------------------------------*/
public class fuzzyLogic {
  public static void main(String[] args) {
  convexFlow controller = new convexFlow();
  volume(controller);
  }
  static void volume(signal type){
  type.patch();
  }
}
