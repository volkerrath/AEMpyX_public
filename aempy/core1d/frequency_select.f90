      MODULE frequency_select
!
!------------------------------------------------------------------------
! LAST CHANGE:   14 Aug 2016   VR  
!------------------------------------------------------------------------
! 
      IMPLICIT NONE
      INTEGER , PARAMETER :: nf_md2 = 46 , nf_6pde = 67
      
!  FRQ_MD2 has 3 frequencies / decade from 0.001 to 1 Hz &
!              6 frequencies / decade from 1.0 to 1MHz
!      REAL(KIND=8) , dimension(nf_md2)  :: frq_md2  =    (/                   &                  
      REAL(KIND=8) , dimension(46)  :: frq_md2  =    (/                   &                  
    &     0.10000000D-02 , 0.21544347D-02 ,                            &
     &     0.46415888D-02 , 0.10000000D-01 , 0.21544347D-01 ,           &
     &     0.46415888D-01 , 0.10000000D+00 , 0.21544347D+00 ,           &
     &     0.46415888D+00 , 0.10000000D+01 , 0.14677993D+01 ,           &
     &     0.21544347D+01 , 0.31622777D+01 , 0.46415888D+01 ,           &
     &     0.68129207D+01 , 0.10000000D+02 , 0.14677993D+02 ,           &
     &     0.21544347D+02 , 0.31622777D+02 , 0.46415888D+02 ,           &
     &     0.68129207D+02 , 0.10000000D+03 , 0.14677993D+03 ,           &
     &     0.21544347D+03 , 0.31622777D+03 , 0.46415888D+03 ,           &
     &     0.68129207D+03 , 0.10000000D+04 , 0.14677993D+04 ,           &
     &     0.21544347D+04 , 0.31622777D+04 , 0.46415888D+04 ,           &
     &     0.68129207D+04 , 0.10000000D+05 , 0.14677993D+05 ,           &
     &     0.21544347D+05 , 0.31622777D+05 , 0.46415888D+05 ,           &
     &     0.68129207D+05 , 0.10000000D+06 , 0.14677993D+06 ,           &
     &     0.21544347D+06 , 0.31622777D+06 , 0.46415888D+06 ,           &
     &     0.68129207D+06 , 0.10000000D+07/)
     
!  FRQ_6PDD has 6 frequencies / decade from 0.001 to 1 MHz
!      REAL(KIND=8) , dimension(nf_6pde) :: frq_6pde =   (/                    &
      REAL(KIND=8) , dimension(67) :: frq_6pde =   (/                    &
     &     0.10000000D-02 , 0.14677993D-02 ,                            &
     &     0.21544347D-02 , 0.31622777D-02 , 0.46415888D-02 ,           &
     &     0.68129207D-02 , 0.10000000D-01 , 0.14677993D-01 ,           &
     &     0.21544347D-01 , 0.31622777D-01 , 0.46415888D-01 ,           &
     &     0.68129207D-01 , 0.10000000D+00 , 0.14677993D+00 ,           &
     &     0.21544347D+00 , 0.31622777D+00 , 0.46415888D+00 ,           &
     &     0.68129207D+00 , 0.10000000D+01 , 0.14677993D+01 ,           &
     &     0.21544347D+01 , 0.31622777D+01 , 0.46415888D+01 ,           &
     &     0.68129207D+01 , 0.10000000D+02 , 0.14677993D+02 ,           &
     &     0.21544347D+02 , 0.31622777D+02 , 0.46415888D+02 ,           &
     &     0.68129207D+02 , 0.10000000D+03 , 0.14677993D+03 ,           &
     &     0.21544347D+03 , 0.31622777D+03 , 0.46415888D+03 ,           &
     &     0.68129207D+03 , 0.10000000D+04 , 0.14677993D+04 ,           &
     &     0.21544347D+04 , 0.31622777D+04 , 0.46415888D+04 ,           &
     &     0.68129207D+04 , 0.10000000D+05 , 0.14677993D+05 ,           &
     &     0.21544347D+05 , 0.31622777D+05 , 0.46415888D+05 ,           &
     &     0.68129207D+05 , 0.10000000D+06 , 0.14677993D+06 ,           &
     &     0.21544347D+06 , 0.31622777D+06 , 0.46415888D+06 ,           &
     &     0.68129207D+06 , 0.10000000D+07 , 0.14677993D+07 ,           &
     &     0.21544347D+07 , 0.31622777D+07 , 0.46415888D+07 ,           &
     &     0.68129207D+07 , 0.10000000D+08 , 0.14677993D+08 ,           &
     &     0.21544347D+08 , 0.31622777D+08 , 0.46415888D+08 ,           &
     &     0.68129207D+08 , 0.10000000D+09/)
     SAVE
    END MODULE frequency_select
