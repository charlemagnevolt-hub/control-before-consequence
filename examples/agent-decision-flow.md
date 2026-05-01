# Example: Agent Decision Flow

An agent attempts to execute an action:

> "Deploy update to production"


## Traditional Model

- Action executed  
- Monitoring detects failure  
- Rollback triggered  


## Control Model

- Action proposed  
- Dependencies analyzed  
- Constraint violation detected  
- Action blocked before execution  


## Result

Failure never materializes.
