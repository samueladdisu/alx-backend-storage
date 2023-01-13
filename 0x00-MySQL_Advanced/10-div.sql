-- SAFE DIV Function
DELIMITER ~
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
DECLARE res FLOAT;
IF b=0 THEN SET res=0;
ELSE SET res=a/b;
END IF;
RETURN res;
END~
