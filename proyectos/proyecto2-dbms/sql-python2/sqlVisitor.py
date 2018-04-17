# Generated from .\sql.g4 by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by sqlParser.

class sqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by sqlParser#parse.
    def visitParse(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#error.
    def visitError(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#sql_stmt_list.
    def visitSql_stmt_list(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#sql_stmt.
    def visitSql_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#create_database_stmt.
    def visitCreate_database_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#alter_database_stmt.
    def visitAlter_database_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#drop_database_stmt.
    def visitDrop_database_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#show_databases_stmt.
    def visitShow_databases_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#show_tables_stmt.
    def visitShow_tables_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#use_database_stmt.
    def visitUse_database_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#alter_table_stmt.
    def visitAlter_table_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#show_columns_stmt.
    def visitShow_columns_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#begin_stmt.
    def visitBegin_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#commit_stmt.
    def visitCommit_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#factored_select_stmt.
    def visitFactored_select_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#create_index_stmt.
    def visitCreate_index_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#create_table_stmt.
    def visitCreate_table_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#delete_stmt.
    def visitDelete_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#drop_index_stmt.
    def visitDrop_index_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#drop_table_stmt.
    def visitDrop_table_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#insert_stmt.
    def visitInsert_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#rollback_stmt.
    def visitRollback_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#simple_select_stmt.
    def visitSimple_select_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#update_stmt.
    def visitUpdate_stmt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#column_def.
    def visitColumn_def(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#type_name.
    def visitType_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#column_constraint.
    def visitColumn_constraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprFunction.
    def visitExprFunction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprNot.
    def visitExprNot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprLiteralValue.
    def visitExprLiteralValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprComparisonSecond.
    def visitExprComparisonSecond(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprLike.
    def visitExprLike(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprNotExists.
    def visitExprNotExists(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprUnaryExpr.
    def visitExprUnaryExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprNotIn.
    def visitExprNotIn(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprNotNull.
    def visitExprNotNull(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprTableColumn.
    def visitExprTableColumn(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprComparisonFirst.
    def visitExprComparisonFirst(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprOr.
    def visitExprOr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprMul.
    def visitExprMul(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprAdd.
    def visitExprAdd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprAnd.
    def visitExprAnd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprParenthesis.
    def visitExprParenthesis(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#exprIsNot.
    def visitExprIsNot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#foreign_key_clause.
    def visitForeign_key_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#table_constraint.
    def visitTable_constraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#ordering_term.
    def visitOrdering_term(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#common_table_expression.
    def visitCommon_table_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#resultColumnAsterisk.
    def visitResultColumnAsterisk(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#resultColumnTableAsterisk.
    def visitResultColumnTableAsterisk(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#resultColumnExpr.
    def visitResultColumnExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#table_or_subquery.
    def visitTable_or_subquery(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#join_clause.
    def visitJoin_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#join_operator.
    def visitJoin_operator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#join_constraint.
    def visitJoin_constraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#select_core.
    def visitSelect_core(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#compound_operator.
    def visitCompound_operator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#cte_table_name.
    def visitCte_table_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#signed_number.
    def visitSigned_number(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#literal_value.
    def visitLiteral_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#unary_operator.
    def visitUnary_operator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#error_message.
    def visitError_message(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#module_argument.
    def visitModule_argument(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#column_alias.
    def visitColumn_alias(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#keyword.
    def visitKeyword(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#name.
    def visitName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#function_name.
    def visitFunction_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#database_name.
    def visitDatabase_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#table_name.
    def visitTable_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#table_or_index_name.
    def visitTable_or_index_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#new_table_name.
    def visitNew_table_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#new_database_name.
    def visitNew_database_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#column_name.
    def visitColumn_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#collation_name.
    def visitCollation_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#foreign_table.
    def visitForeign_table(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#index_name.
    def visitIndex_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#trigger_name.
    def visitTrigger_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#view_name.
    def visitView_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#module_name.
    def visitModule_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#table_alias.
    def visitTable_alias(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#transaction_name.
    def visitTransaction_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#any_name.
    def visitAny_name(self, ctx):
        return self.visitChildren(ctx)


