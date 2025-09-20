!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!                            |
!         FM-Pool            |  Lambda: Thermoelectric Control Engineering
!          9173              |  www.optaphy.com
!                            |
!-------------------------------------------------------------------------------
!   Copyright (C) 2024 Lambda KG
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
program central_diff
  implicit none
  integer, parameter :: nx = 6, ny = 6
  real :: dx, dy, u(nx,ny)
  integer :: i, j
  integer :: impedance = 1
  do j = 1,6
    do i = 1,6
      u(i,j)=impedance**3
      impedance=impedance+1
    end do
  end do
  u(0,0) = 0.5
  u(4,3) = 264
  open(1, file = 'heat_map_data.csv', status = 'new')
  do i = 1,6
     write(1,*) u(i,1), u(i,2), u(i,3), u(i,4), u(i,5), u(i,6)
  end do
end program central_diff
