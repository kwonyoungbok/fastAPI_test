"""create table

Revision ID: 89b38e270954
Revises: 
Create Date: 2022-01-06 15:00:37.348612

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '89b38e270954'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("teacher",
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=32), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('subject',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=64), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('teacher_subject',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('price', sa.Integer, default=0),
                    sa.Column('teacher_id', sa.Integer, nullable=True),
                    sa.Column('subject_id', sa.Integer, nullable=True),

                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ),
                    sa.ForeignKeyConstraint(['subject_id'], ['subject_id.id'], )
                    )


def downgrade():
    op.drop_table('teacher_subject')
    op.drop_table('subject')
    op.drop_table('teacher')
