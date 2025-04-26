CREATE TABLE [dbo].[Files] (

	[Name] varchar(8000) NULL, 
	[Extension] varchar(8000) NULL, 
	[Date accessed] datetime2(6) NULL, 
	[Date modified] datetime2(6) NULL, 
	[Date created] datetime2(6) NULL, 
	[Folder Path] varchar(8000) NULL
);