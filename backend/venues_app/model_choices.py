class SeatChoice:
    available = 'Available'
    reserved = 'Reserved'
    sold = 'Sold'

    STATUS_CHOICES = (
        (available, 'Available'),
        (reserved, 'Reserved'),
        (sold, 'Sold')
    )

class EmployeeChoice:
    manager_rank = 'Manager'
    steward_rank = 'Steward'
    security_rank = 'Security'
    executive_rank = 'Executive'
    trainee_rank = 'Trainee'
    
    TYPE_CHOICES = (
        (manager_rank, 'Manager'),
        (steward_rank, 'Steward'),
        (security_rank, 'Security'),
        (executive_rank, 'Executive'),
        (trainee_rank, 'Trainee')
    )

    contractual = 'Contractual'
    permanent = 'Permanent'
    intern = 'Intern'

    CONTRACT_CHOICES = (
        (contractual, 'Contractual'),
        (permanent, 'Permanent'),
        (intern, 'Intern')
    )