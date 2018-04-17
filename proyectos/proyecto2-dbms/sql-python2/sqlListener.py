# Generated from .\sql.g4 by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete listener for a parse tree produced by sqlParser.
class sqlListener(ParseTreeListener):

    # Enter a parse tree produced by sqlParser#parse.
    def enterParse(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#parse.
    def exitParse(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#error.
    def enterError(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#error.
    def exitError(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#sql_stmt_list.
    def enterSql_stmt_list(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#sql_stmt_list.
    def exitSql_stmt_list(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#sql_stmt.
    def enterSql_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#sql_stmt.
    def exitSql_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#create_database_stmt.
    def enterCreate_database_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#create_database_stmt.
    def exitCreate_database_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#alter_database_stmt.
    def enterAlter_database_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#alter_database_stmt.
    def exitAlter_database_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#drop_database_stmt.
    def enterDrop_database_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#drop_database_stmt.
    def exitDrop_database_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#show_databases_stmt.
    def enterShow_databases_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#show_databases_stmt.
    def exitShow_databases_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#show_tables_stmt.
    def enterShow_tables_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#show_tables_stmt.
    def exitShow_tables_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#use_database_stmt.
    def enterUse_database_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#use_database_stmt.
    def exitUse_database_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#alter_table_stmt.
    def enterAlter_table_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#alter_table_stmt.
    def exitAlter_table_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#show_columns_stmt.
    def enterShow_columns_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#show_columns_stmt.
    def exitShow_columns_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#begin_stmt.
    def enterBegin_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#begin_stmt.
    def exitBegin_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#commit_stmt.
    def enterCommit_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#commit_stmt.
    def exitCommit_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#factored_select_stmt.
    def enterFactored_select_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#factored_select_stmt.
    def exitFactored_select_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#create_index_stmt.
    def enterCreate_index_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#create_index_stmt.
    def exitCreate_index_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#create_table_stmt.
    def enterCreate_table_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#create_table_stmt.
    def exitCreate_table_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#delete_stmt.
    def enterDelete_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#delete_stmt.
    def exitDelete_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#drop_index_stmt.
    def enterDrop_index_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#drop_index_stmt.
    def exitDrop_index_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#drop_table_stmt.
    def enterDrop_table_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#drop_table_stmt.
    def exitDrop_table_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#insert_stmt.
    def enterInsert_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#insert_stmt.
    def exitInsert_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#rollback_stmt.
    def enterRollback_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#rollback_stmt.
    def exitRollback_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#simple_select_stmt.
    def enterSimple_select_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#simple_select_stmt.
    def exitSimple_select_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#update_stmt.
    def enterUpdate_stmt(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#update_stmt.
    def exitUpdate_stmt(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#column_def.
    def enterColumn_def(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#column_def.
    def exitColumn_def(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#type_name.
    def enterType_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#type_name.
    def exitType_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#column_constraint.
    def enterColumn_constraint(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#column_constraint.
    def exitColumn_constraint(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprFunction.
    def enterExprFunction(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprFunction.
    def exitExprFunction(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprNot.
    def enterExprNot(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprNot.
    def exitExprNot(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprLiteralValue.
    def enterExprLiteralValue(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprLiteralValue.
    def exitExprLiteralValue(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprComparisonSecond.
    def enterExprComparisonSecond(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprComparisonSecond.
    def exitExprComparisonSecond(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprLike.
    def enterExprLike(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprLike.
    def exitExprLike(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprNotExists.
    def enterExprNotExists(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprNotExists.
    def exitExprNotExists(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprUnaryExpr.
    def enterExprUnaryExpr(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprUnaryExpr.
    def exitExprUnaryExpr(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprNotIn.
    def enterExprNotIn(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprNotIn.
    def exitExprNotIn(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprNotNull.
    def enterExprNotNull(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprNotNull.
    def exitExprNotNull(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprTableColumn.
    def enterExprTableColumn(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprTableColumn.
    def exitExprTableColumn(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprComparisonFirst.
    def enterExprComparisonFirst(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprComparisonFirst.
    def exitExprComparisonFirst(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprOr.
    def enterExprOr(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprOr.
    def exitExprOr(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprMul.
    def enterExprMul(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprMul.
    def exitExprMul(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprAdd.
    def enterExprAdd(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprAdd.
    def exitExprAdd(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprAnd.
    def enterExprAnd(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprAnd.
    def exitExprAnd(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprParenthesis.
    def enterExprParenthesis(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprParenthesis.
    def exitExprParenthesis(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#exprIsNot.
    def enterExprIsNot(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#exprIsNot.
    def exitExprIsNot(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#foreign_key_clause.
    def enterForeign_key_clause(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#foreign_key_clause.
    def exitForeign_key_clause(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#table_constraint.
    def enterTable_constraint(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#table_constraint.
    def exitTable_constraint(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#ordering_term.
    def enterOrdering_term(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#ordering_term.
    def exitOrdering_term(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#common_table_expression.
    def enterCommon_table_expression(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#common_table_expression.
    def exitCommon_table_expression(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#resultColumnAsterisk.
    def enterResultColumnAsterisk(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#resultColumnAsterisk.
    def exitResultColumnAsterisk(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#resultColumnTableAsterisk.
    def enterResultColumnTableAsterisk(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#resultColumnTableAsterisk.
    def exitResultColumnTableAsterisk(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#resultColumnExpr.
    def enterResultColumnExpr(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#resultColumnExpr.
    def exitResultColumnExpr(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#table_or_subquery.
    def enterTable_or_subquery(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#table_or_subquery.
    def exitTable_or_subquery(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#join_clause.
    def enterJoin_clause(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#join_clause.
    def exitJoin_clause(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#join_operator.
    def enterJoin_operator(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#join_operator.
    def exitJoin_operator(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#join_constraint.
    def enterJoin_constraint(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#join_constraint.
    def exitJoin_constraint(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#select_core.
    def enterSelect_core(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#select_core.
    def exitSelect_core(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#compound_operator.
    def enterCompound_operator(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#compound_operator.
    def exitCompound_operator(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#cte_table_name.
    def enterCte_table_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#cte_table_name.
    def exitCte_table_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#signed_number.
    def enterSigned_number(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#signed_number.
    def exitSigned_number(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#literal_value.
    def enterLiteral_value(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#literal_value.
    def exitLiteral_value(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#unary_operator.
    def enterUnary_operator(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#unary_operator.
    def exitUnary_operator(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#error_message.
    def enterError_message(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#error_message.
    def exitError_message(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#module_argument.
    def enterModule_argument(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#module_argument.
    def exitModule_argument(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#column_alias.
    def enterColumn_alias(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#column_alias.
    def exitColumn_alias(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#keyword.
    def enterKeyword(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#keyword.
    def exitKeyword(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#name.
    def enterName(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#name.
    def exitName(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#function_name.
    def enterFunction_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#function_name.
    def exitFunction_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#database_name.
    def enterDatabase_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#database_name.
    def exitDatabase_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#table_name.
    def enterTable_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#table_name.
    def exitTable_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#table_or_index_name.
    def enterTable_or_index_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#table_or_index_name.
    def exitTable_or_index_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#new_table_name.
    def enterNew_table_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#new_table_name.
    def exitNew_table_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#new_database_name.
    def enterNew_database_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#new_database_name.
    def exitNew_database_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#column_name.
    def enterColumn_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#column_name.
    def exitColumn_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#collation_name.
    def enterCollation_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#collation_name.
    def exitCollation_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#foreign_table.
    def enterForeign_table(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#foreign_table.
    def exitForeign_table(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#index_name.
    def enterIndex_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#index_name.
    def exitIndex_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#trigger_name.
    def enterTrigger_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#trigger_name.
    def exitTrigger_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#view_name.
    def enterView_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#view_name.
    def exitView_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#module_name.
    def enterModule_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#module_name.
    def exitModule_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#table_alias.
    def enterTable_alias(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#table_alias.
    def exitTable_alias(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#transaction_name.
    def enterTransaction_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#transaction_name.
    def exitTransaction_name(self, ctx):
        pass


    # Enter a parse tree produced by sqlParser#any_name.
    def enterAny_name(self, ctx):
        pass

    # Exit a parse tree produced by sqlParser#any_name.
    def exitAny_name(self, ctx):
        pass


