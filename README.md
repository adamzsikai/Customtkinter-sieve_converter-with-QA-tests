I. Project Name:  
  1. sieve_converter
       
II. Technology Stack  
  1. Programming language: Python  
  2. User Interface: CustomTkinter (GUI-based desktop   
  application)

III. Purpose  
  1. The sieve_converter application provides standardized   
  sieve size conversions between mesh, micron, and millimeter   
  units, following industry-standard sieve sizes only, where   
  applicable.  
  2. The application is intended for repeated, uninterrupted   
  use in an industrial or laboratory context.
 
IV. Supported Conversions and Constraints  
  1. Conversions limited to existing industry sieve sizes  
  2. The following conversions must only be performed using   
  predefined, industry-standard sieve size mappings. If the input   
  value does not exist in the internal sieve table, the   
  conversion must be rejected with an error message.  
  3. Mesh → Micron  
  4. Mesh → Millimeter  
  5. Micron → Mesh  
  6. Millimeter → Mesh
     
V. Free numerical conversions  
  1. The following conversions may accept any valid positive   
  numeric value:  
  2. Micron → Millimeter  
  3. Millimeter → Micron
     
VI. Input Requirements  
  1. Mandatory Inputs  
  2. The application requires all of the following inputs before   
  performing a conversion:  
  3. Sieve Size  
  4. Must be a numeric value  
  5. Must be positive (negative values are not allowed)  
  6. Example: 60  
  7. FROM Unit  
  8. Must be selected from a dropdown menu  
  9. Available options: MESH, MICRON, MILLIMETER  
  10. TO Unit  
  11. Must be selected from a dropdown menu  
  12. Available options: MESH, MICRON, MILLIMETER
      
VII. Decimal Format Rules  
  1. For millimeter inputs, only dot (.) is accepted as a   
  decimal separator  
  2. Valid: 0.841  
  3. Invalid: 0,841
     
VIII. Output  
  1. The result must be displayed clearly in the GUI after a   
  successful conversion.  
  2. Example:  
  3. Input: 60 MESH → MICRON  
  4. Output: 250 MICRON
     
IX. Validation and Error Handling  
  1. The application must implement the following   
  validations:  
  2. Mandatory input fields must not be empty.  
  3. FROM and TO units must be selected.  
  4. Negative values must be rejected.  
  5. Non-numeric input must be rejected.  
  6. Invalid decimal format (comma instead of dot) must be   
  rejected.
  7. Conversions using non-existing sieve sizes (where   
  industry limitation applies) must be rejected.
 
X. Error Feedback  
  1. All validation errors must be communicated via a clear,   
  user-visible error message.  
  2. Error messages must be descriptive and actionable (e.g.   
  “Selected sieve size does not exist in the standard sieve   
  table”).

XI. GUI and Usability Requirements  
1. The GUI must be user-friendly and visually clear.  
2. Proper color contrast must be used for:  
3. Labels  
4. Input fields  
5. Result display  
6. Error messages  
7. The application must support multiple consecutive   
conversions without restarting.  
8. Input fields and result areas must refresh correctly   
between conversions.
