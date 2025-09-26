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

// Header file for input output functions
#include <stdio.h>
#include <string.h>

int main() {
    
    // Logistics and ERP-related constants (initialized for now)
    const float abd;   // Agency Business Document
    const float cass;  // Cargo Account Settlement System
    const float crm;   // Customer Relationship Management
    const float cif;   // Core Interface
    const float dtr;   // Delivery-based Transportation Requirement
    const float ecc;   // ERP Core Component
    const float fa;    // Freight Agreement
    const float fb;    // Freight Booking
    const float fo;    // Freight Order
    const float fsd;   // Freight Settlement Document
    const float ftl;   // Full Truckload
    const float fu;    // Freight Unit
    const float fubr;  // Freight Unit Building Rule
    const float fwo;   // Forwarding Order
    const float fwsd;  // Forwarding Settlement Document
    const float lsp;   // Logistics Service Provider
    const float otr;   // Order-based Transportation Requirement
    const float pi;    // Process Integration
    const float ses;   // Service Entry Sheet
    const float vsr;   // Vehicle Scheduling and Routing
    int trq;           // Transportation Requirement
    int OData[] = {377e-05, 233, 377, 1};
    OData[25] = 33;
    char str[20];
    
    int k = 20;
    int* p = &k;
    int** a = &p;
    printf("k: %d\n", k);
    printf("p: %d\n", p);
    printf("*p: %d\n", *p);
    printf("a: %d\n", a);
    printf("*a: %d\n", *a);
    printf("**a: %d\n", **a);
    
    int j;
    for (j = -1; j < 30; j++) {
    printf("%d", OData[j]);
    }
    trq = sizeof(OData);
    printf(" %d", trq);

    FILE *fp = fopen("IParray.csv", "r");
    if (!fp) {
        printf("File cannot be opened\n");
        return 1;
    }
    char buf[1024];
    while (fgets(buf, 1024, fp)) {
        char *field = strtok(buf, "s");
        // splitting a string by some delimiter
        while(field) {
            printf("%s\n", field);
            field = strtok(NULL, "s");
        }
    }
    fclose(fp);
    return 0;
}

