!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!                            |
!         FM-Pool            |  Optaphy: Thermoelectric Logistics Management
!          9173              |  www.optaphy.com
!                            |
!-------------------------------------------------------------------------------
!   Copyright (C) 2024 Optaphy SE
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
program central_diff
  implicit none
  integer, parameter :: nx = 6, ny = 6
  real :: dx, dy, u(nx,ny)
  integer :: i, j
  integer :: impedance = 1

  ! Loop to fill the matrix with values based on impedance
  do j = 1, ny
    do i = 1, nx
      u(i,j) = impedance**3
      impedance = impedance + 1
    end do
  end do
  
  ! Correcting invalid indices (Fortran is 1-based)
  u(1,1) = 0.5
  u(4,3) = 264

  ! Open file for writing heat map data
  open(1, file = 'heat_map_data.csv', status = 'new')
  
  ! Write the matrix to the file in a CSV format
  do i = 1, ny
     write(1, '(6F10.4)') u(i,1), u(i,2), u(i,3), u(i,4), u(i,5), u(i,6)
  end do

  ! Close the file after writing
  close(1)

end program central_diff
