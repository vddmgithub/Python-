"""
  Q: What are the types of tables in HIVE? What is the basic difference between them?

Ans: There are two types of tables in Hive ,one is Managed table and second is external table.
     The difference is , when you drop a table, if it is managed table hive deletes both data and meta data,if it is external table Hive only deletes metadata.

  Q: What is the difference between schema on Read vs Schema on write and Hive belong to which category.

Ans: Schema-on-Read vs. Schema-on-Write:

    In RDMS databases,
            Table's schema is imposed during the data load time, if the data being loaded does not confirm to the schema
                then the data load is rejected, and hence it Schema-on-Write.
            Here the data is being checked against the schema when written into the database(during data load).

    In HIVE, the data schema is not verified during the load time, rather it is verified while processing the query.
    Hence this process in HIVE called Schema-on-Read.

  Q: How to use the Python UDF once it is registered

Ans: Once the mapper is registered, we need to apply the mapper(UDF) on the table that we are interested which performs the transformation.
     Its good practice to apply UDF and load the resultant into a new table.

  Q: What are the ways to invoke PIG in CLI mode?

Ans: PIG is a data flow language. PIG is also been build on top of Map Reduce.
    1. Pig in local interactive mode
    2. Pig in Map Reduce Mode
    3. Pig in Tez Mode
    4. Pig separate scripts in local interactive mode or Map Reduce mode

  Q: How to view step by step executions of a sequence of statements for a relation in PIG?

Ans: Need to illustrate command to view the sequence of steps that are executed in PIG.


  Q: How to let PIG know where the output of UDF will go?

Ans: You have to pass the location,
     Example: STORE outval INTO '/user/root/Pig-Output_$TS' ...

"""
