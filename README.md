# SHPB Analysis 
## Explanation for Stress-Strain Calculation in SHPB Experiment

In the Split Hopkinson Pressure Bar (SHPB) experiment, the characteristic relations associated with one-dimensional elastic wave propagation in the bar provide the basis for calculating stress and strain in the specimen.

1. **Particle Velocity at Specimen/Input-Bar and Specimen/Output-Bar Interface:**
   - The particle velocity $` v_1(t) `$ at the specimen/input-bar interface is given by:
     $` v_1(t) = c_b(\varepsilon_I - \varepsilon_R) `$ 
   - Here, $` c_b = \sqrt{\frac{E_b}{\rho_b}} `$ represents the bar wave speed, with $` E_b `$ denoting the Young's modulus and $` \rho_b `$ the density of the bar material.
   - The particle velocity $` v_2(t) `$ at the specimen/output-bar interface is given by:
     $` v_2(t) = c_b \varepsilon_T `$ 

2. **Mean Axial Strain Rate in the Specimen:**
   - The mean axial strain rate $` \dot{e}_s `$ in the specimen is calculated as:
     $` \dot{e}_s = \frac{c_b}{l_0} (\varepsilon_I - \varepsilon_R - \varepsilon_T) = \frac{v_1 - v_2}{l_0} `$ 
   - Here, $` l_0 `$ represents the initial specimen length.

3. **Calculation of Bar Stresses and Normal Forces:**
   - The stresses and normal forces at the specimen/bar interfaces are computed as follows:
     - $` P_1 = E_b (\varepsilon_I + \varepsilon_R) A_b `$ at the specimen/input-bar interface.
     - $` P_2 = E_b \varepsilon_T A_b `$ at the specimen/output-bar interface.
   - Here, $` A_b `$ denotes the cross-sectional area of the bars.

4. **Mean Axial Stress in the Specimen:**
   - The mean axial stress $` \bar{S}_s(t) `$ in the specimen is given by:
     $` \bar{S}_s(t) = \frac{(P_1 + P_2)}{2} \left( \frac{1}{A_s} \right) `$ 
   - Here, $` A_s `$ represents the initial cross-sectional area of the specimen.

5. **Stress-Strain Relationship:**
   - Assuming stress equilibrium, uniaxial stress conditions in the specimen, and one-dimensional elastic stress wave propagation without dispersion in the bars, the nominal strain rate $` \dot{e}_s `$, nominal strain $` e_s `$, and nominal stress $` S_s `$ in the specimen are estimated using:
     -  $` \dot{e}_s(t) = \frac{2c_b}{l_0} \varepsilon_R(t) `$ 
     -  $` e_s(t) = \int_0^t \dot{e}_s(\tau) d\tau `$ 
     -  $` S_s(t) = \frac{E_b A_b}{A_s} \varepsilon_T(t) `$
    
6. **True Stress-Strain:**
   - True strain $\varepsilon_s(t)$ in the specimen is given by:
      - $\varepsilon_s(t) = -\ln(1 - e_s(t))$   <br />
     Here, $e_s(t)$ represents the engineering strain in the specimen.

   - The true strain rate $\dot{\varepsilon}_s(t)$ in the specimen is calculated as:
      - $\dot{\varepsilon}_s(t) = \frac{\dot{e}_s(t)}{1 - e_s(t)}$

   - The true stress $\sigma_s(t)$ in the specimen is obtained as:
        - $\sigma_s(t) = S_s(t) \cdot (1 - e_s(t))$    <br />
     Here, $S_s(t)$ represents the nominal stress in the specimen.


### Reference

The theory and equations used in this project are based on the following sources:

- K.T. Ramesh, *Handbook of Experimental Solid Mechanics* (Chapter 33: High Rates and Impact Experiments), Springer, 2008.




