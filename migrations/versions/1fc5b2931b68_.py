"""empty message

Revision ID: 1fc5b2931b68
Revises: 
Create Date: 2021-06-22 01:37:47.955453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fc5b2931b68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dept',
    sa.Column('DeptNum', sa.String(length=4), nullable=False),
    sa.Column('DeptName', sa.String(length=10), nullable=False),
    sa.Column('DeptChairman', sa.String(length=10), nullable=False),
    sa.Column('DeptTel', sa.String(length=11), nullable=True),
    sa.Column('DeptDesc', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('DeptNum')
    )
    op.create_table('manager',
    sa.Column('ManagerNum', sa.String(length=8), nullable=False),
    sa.Column('ManagerName', sa.String(length=10), nullable=False),
    sa.Column('ManagerSex', sa.String(length=2), nullable=False),
    sa.Column('ManagerBirthday', sa.DateTime(), nullable=True),
    sa.Column('ManagerPassword', sa.Text(), nullable=False),
    sa.Column('ManagerPermission', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('ManagerNum')
    )
    op.create_table('selector_student',
    sa.Column('SelectorStudentNum', sa.String(length=8), nullable=False),
    sa.PrimaryKeyConstraint('SelectorStudentNum')
    )
    op.create_table('training_program',
    sa.Column('TPNumber', sa.String(length=7), nullable=False),
    sa.PrimaryKeyConstraint('TPNumber')
    )
    op.create_table('course',
    sa.Column('CourseNum', sa.String(length=8), nullable=False),
    sa.Column('CourseName', sa.String(length=10), nullable=False),
    sa.Column('CourseCredit', sa.Integer(), nullable=False),
    sa.Column('CourseTime', sa.Integer(), nullable=False),
    sa.Column('CourseDesc', sa.Text(), nullable=True),
    sa.Column('DeptNum', sa.String(length=4), nullable=False),
    sa.ForeignKeyConstraint(['DeptNum'], ['dept.DeptNum'], ),
    sa.PrimaryKeyConstraint('CourseNum')
    )
    op.create_table('major',
    sa.Column('MajorNum', sa.String(length=6), nullable=False),
    sa.Column('DeptNum', sa.String(length=4), nullable=False),
    sa.Column('MajorName', sa.String(length=10), nullable=False),
    sa.Column('MajorAssistant', sa.String(length=10), nullable=False),
    sa.Column('MajorTel', sa.String(length=11), nullable=True),
    sa.Column('MajorDesc', sa.Text(), nullable=True),
    sa.Column('TrainingProgram', sa.String(length=7), nullable=True),
    sa.ForeignKeyConstraint(['DeptNum'], ['dept.DeptNum'], ),
    sa.PrimaryKeyConstraint('MajorNum')
    )
    op.create_table('teacher',
    sa.Column('TeacherNum', sa.String(length=8), nullable=False),
    sa.Column('DeptNum', sa.String(length=4), nullable=False),
    sa.Column('TeacherName', sa.String(length=10), nullable=False),
    sa.Column('TeacherSex', sa.String(length=2), nullable=False),
    sa.Column('TeacherInyear', sa.String(length=4), nullable=False),
    sa.Column('TeacherTitle', sa.String(length=10), nullable=True),
    sa.Column('TeacherPassword', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['DeptNum'], ['dept.DeptNum'], ),
    sa.PrimaryKeyConstraint('TeacherNum')
    )
    op.create_table('course_teacher',
    sa.Column('CourseNum', sa.String(length=8), nullable=False),
    sa.Column('TeacherNum', sa.String(length=10), nullable=False),
    sa.Column('CourseCapacity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['CourseNum'], ['course.CourseNum'], ),
    sa.ForeignKeyConstraint(['TeacherNum'], ['teacher.TeacherNum'], ),
    sa.PrimaryKeyConstraint('CourseNum', 'TeacherNum')
    )
    op.create_table('student',
    sa.Column('StudentNum', sa.String(length=10), nullable=False),
    sa.Column('MajorNum', sa.String(length=16), nullable=False),
    sa.Column('StudentName', sa.String(length=10), nullable=False),
    sa.Column('StudentSex', sa.String(length=10), nullable=False),
    sa.Column('StudentInyear', sa.String(length=4), nullable=False),
    sa.Column('StudengtPassword', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['MajorNum'], ['major.MajorNum'], ),
    sa.PrimaryKeyConstraint('StudentNum')
    )
    op.create_table('course_select_table',
    sa.Column('StudentNum', sa.String(length=8), nullable=False),
    sa.Column('CourseNum', sa.String(length=10), nullable=False),
    sa.Column('TeacherNum', sa.String(length=8), nullable=False),
    sa.Column('Grade', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['CourseNum'], ['course.CourseNum'], ),
    sa.ForeignKeyConstraint(['StudentNum'], ['student.StudentNum'], ),
    sa.ForeignKeyConstraint(['TeacherNum'], ['teacher.TeacherNum'], ),
    sa.PrimaryKeyConstraint('StudentNum', 'CourseNum', 'TeacherNum')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('course_select_table')
    op.drop_table('student')
    op.drop_table('course_teacher')
    op.drop_table('teacher')
    op.drop_table('major')
    op.drop_table('course')
    op.drop_table('training_program')
    op.drop_table('selector_student')
    op.drop_table('manager')
    op.drop_table('dept')
    # ### end Alembic commands ###
