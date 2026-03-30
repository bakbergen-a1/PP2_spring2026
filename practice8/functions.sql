CREATE OR REPLACE FUNCTION search_contacts(word TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.phone
    FROM contacts c
    WHERE c.name ILIKE '%' || word || '%'
       OR c.phone ILIKE '%' || word || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_page(lim INT, offs INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM contacts c
    LIMIT lim OFFSET offs;
END;
$$ LANGUAGE plpgsql;